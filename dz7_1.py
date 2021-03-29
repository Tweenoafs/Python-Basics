import os

subdir = ['settings', 'mainapp', 'adminapp', 'authapp']
for el in subdir:
    dir_path = os.path.join('my_project', el)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
