import glob
import gym
import os
import random

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

class VimEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def get_random_challenge():
        return random.choice(glob.glob(ROOT_DIR + '/data/*/*'))

    # OpenAI gym Env required functions

    def __init__(self, challenge=None):
        pass

    def _step(self, action):
        pass

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        pass
