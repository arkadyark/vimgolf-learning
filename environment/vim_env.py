import gym
import os
from edblib import align
from tree import get_random_challenge, get_challenge_infile, get_challenge_outfile
import environment.utils.run_command as _run_command

class VimEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    MAX_ACTIONS = 100
    TEMP_FILENAME = 'temp_infile.txt'

    # OpenAI gym Env required functions

    def __init__(self, challenge_id=None):
        if not challenge_id:
            challenge_id = get_random_challenge()
        self.infile = get_challenge_infile(challenge_id)
        self.outfile = get_challenge_outfile(challenge_id)
        self.actions = []

    def run_command(self):
        _run_command(''.join(self.actions), VimEnv.TEMP_FILENAME)

    def distance(self, contents):
        return align(contents, self.outfile)['editDistance']

    def get_state(self):
        return {}

    def _step(self, action):
        self.actions.append(action)
        if len(self.actions) >= VimEnv.MAX_ACTIONS:
            return None, -VimEnv.MAX_ACTIONS, True, {}
        with open(VimEnv.TEMP_FILENAME, 'w+') as f:
            f.write(self.infile)
        self.run_command(''.join(self.actions), 'temp_infile.txt')
        with open(VimEnv.TEMP_FILENAME, 'w+') as f:
            contents = f.read()
            distance = self.distance(contents)
            if distance == 0:
                return None, 100, True, {}
            else:
                return self.get_state(), -distance, False, {}

    def _reset(self):
        try:
            os.remove(VimEnv.TEMP_FILENAME)
        except OSError:
            pass

    def _render(self, mode='human', close=False):
        print("Actions: {}".format(''.join(self.actions)))
        with open(VimEnv.TEMP_FILENAME) as f:
            print("File: {}".format(f.read()))
