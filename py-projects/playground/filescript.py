#filesript.py: Moves text files in selected folder to dedicated directory

import shutil, os, send2trash, zipfile

for folder, subfolders, files in os.walk('py-projects'):
    print(f'The current folder is {folder}')
    for sub in subfolders:
        print(f'{sub} is in {folder}')
        print('....')
    for file in files:
        print(f'{file} can be found in {folder}')
        
    print('....')

# playfiles = os.listdir('py-projects/playground')

# def check_move():
#     for file in playfiles:
#         if file.endswith('.txt'):
#             txtfile = os.path.join('py-projects/playground', file)
#             print(f'Found {file}')
#             shutil.move(txtfile, 'py-projects/textfiles')
            

# for file in playfiles:
#     print(file)

# check_move()
# print('Moved files to \'textfiles\' directory')