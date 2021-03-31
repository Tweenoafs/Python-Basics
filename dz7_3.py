import os
from shutil import copytree


def replace_dir():
    from_dir = 'my_project'
    to_dir = 'templates'

    for root, dirs, files in os.walk(from_dir):
        if root.find(to_dir) > 0 and len(files) == 0:
            copytree(os.path.join(root), to_dir, dirs_exist_ok=True)


if __name__ == '__main__':
    replace_dir()
