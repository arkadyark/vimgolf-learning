import subprocess
import os

def run_command(command, edit_file):
    subprocess.call('vim -c "let @a=\'{}\'" -c \"normal! @a\" -c \"pyfile current_state.py" {} -c \"normal! \x1bZZ\"'.format(command, edit_file), shell=True)

if __name__ == '__main__':
    for i in range(1):
        run_command('iabc\x1bV', os.path.expanduser('test.txt'))
