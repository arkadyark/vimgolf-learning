import gym
from gym.spaces import Discrete
from edlib import align
from tree import get_random_challenge, get_challenge_infile, get_challenge_outfile
from tree import get_state
from environment.utils.run_command import run_command
from environment.utils.constants import REGISTERS, VOCAB

class VimEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    MAX_ACTIONS = 100
    TEMP_FILENAME = 'temp_infile.txt'

    # OpenAI gym Env required functions

    def __init__(self):
        self.action_space = Discrete(len(VOCAB))

    def distance(self, contents):
        return align(contents, self.outfile)['editDistance']

    def step(self, action):
        self.actions.append(VOCAB[action])
        if len(self.actions) >= VimEnv.MAX_ACTIONS:
            return None, -VimEnv.MAX_ACTIONS*100, True, {}
        with open(VimEnv.TEMP_FILENAME, 'w+') as f:
            f.write(self.infile)
        run_command(''.join(self.actions), VimEnv.TEMP_FILENAME)
        with open(VimEnv.TEMP_FILENAME) as f:
            self.state = get_state()
            distance = self.distance(self.state['contents'])
            if distance == 0:
                return None, 10000, True, {}
            else:
                return self.state, -distance, False, {}

    def reset(self):
        challenge_id = get_random_challenge()
        self.infile = get_challenge_infile(challenge_id)
        self.outfile = get_challenge_outfile(challenge_id)
        self.actions = []
        self.state = {'mode': '', 'cursor': (1, 1)}
        with open(VimEnv.TEMP_FILENAME, 'w+') as f:
            f.write(self.infile)

        return {'contents': self.infile,
                'registers': ['' for i in range(len(REGISTERS))],
                'cursor': (0, 0),
                'mode': 'n'}

    def render(self, mode='human', close=False):
        print("========= Actions ========")
        print(''.join(self.actions))
        print("========= File ========")
        with open(VimEnv.TEMP_FILENAME) as f:
            print(f.read())
        print("========= Output File ========")
        print(self.outfile)
        print("========= Mode ========")
        print(self.state['mode'])
        print("========= Cursor ========")
        print(self.state['cursor'])
