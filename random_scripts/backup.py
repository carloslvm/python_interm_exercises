#!/usr/bin/python3

import os

# Step one: File to store
print('Enter the full path of the file you want to backup:')
print('Separate the paths with a comma')
print('Example /home/user/notes.txt, /home/user/README.md')
file_paths = input('Enter paths: ')
source = file_paths.split(',')

# Step two: Create the backup directory
print('\nCreate the directory to backup your files.')
dir_path = input('Enter full path: ')

if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Step three: Name your zip archive
print('\nEnter the name of your zip archive:')
name_zip = input('Enter name: ') + '.zip'
archive = dir_path + os.sep + name_zip

# Setting up zip command
zip_command = 'zip -r {0} {1}'.format(archive, ' '.join(source))

# Running the program
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Archive saved in', dir_path)
else:
    print('Backup Failed')
