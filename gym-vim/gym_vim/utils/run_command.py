import subprocess
import os

def execute_command(command, edit_file):
    with open(os.path.expanduser('~/.vim_runtime/learnvim.vim'), 'w+') as f:
        f.write("let @a='{}'".format(command))
    subprocess.call('vim -c \"normal! @a\" -c \"pyfile current_state.py" {} -c \"normal! \x1bZZ\"'.format(edit_file), shell=True)

if __name__ == '__main__':
    for i in range(5):
        execute_command('iabc\x1bV', os.path.expanduser('~/test.txt'))
