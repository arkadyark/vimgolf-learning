import shutil
import subprocess
import os
from tree import get_state

def run_command(command, edit_file):
    os.rename(os.path.expanduser('~/.vimrc'), 'temp.vimrc')
    shutil.copyfile('environment/vimgolf.vimrc', os.path.expanduser('~/.vimrc'))
    with open(os.path.expanduser('~/.vim_runtime/learnvim.vim'), 'w+') as f:
        f.write("silent let @a='{}'\n".format(command))

    with open(os.path.expanduser('~/.vimrc'), 'a') as f:
        f.write('source ~/.vim_runtime/learnvim.vim')
    subprocess.call('vim -c \"normal! @a\" -c \"pyfile environment/utils/current_state.py" {} -c \"normal! \x1bZZ\"'.format(edit_file), shell=True)
    os.rename('temp.vimrc', os.path.expanduser('~/.vimrc'))

if __name__ == '__main__':
    for i in range(5):
        run_command('iabc\x1bV', 'test.txt')
        print(get_state())
