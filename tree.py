import glob
import os
import random

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_random_challenge():
    return random.choice(glob.glob(ROOT_DIR + '/data/infiles/*')).split('/')[-1].split('.')[0]

def get_challenge_infile(challenge_id):
    with open(ROOT_DIR + '/data/infiles/{}.txt'.format(challenge_id)) as f:
        return f.read()

def get_challenge_outfile(challenge_id):
    with open(ROOT_DIR + '/data/outfiles/{}.txt'.format(challenge_id)) as f:
        return f.read()

def get_state():
    with open("environment/state/registers.txt") as f:
        registers = f.read().split('\t')
    with open("environment/state/contents.txt") as f:
        contents = f.read()
    with open("environment/state/mode.txt") as f:
        mode = f.read()
    with open("environment/state/cursor.txt") as f:
        cursor = f.read().split(' ')
    return {
        'registers': registers,
        'contents': contents,
        'mode': mode,
        'cursor': cursor
    }
