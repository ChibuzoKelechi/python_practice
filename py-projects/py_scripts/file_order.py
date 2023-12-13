#! /usr/bin/env python3
#file_order.py: MOves files of different extensions to corresponding folders

import os, shutil

downloads_folder = '/home/kelechi/Downloads'
download_files = os.listdir(downloads_folder)

def checkfile():
    for file in download_files:
        filepath = os.path.join(downloads_folder, file)
        
        if file.endswith('.txt'):
            shutil.move(filepath, '/home/kelechi/Downloads/textfiles')
        elif file.endswith('.jpg') or file.endswith('.png') or file.endswith('.webp'):
            shutil.move(filepath, '/home/kelechi/Downloads/Images')
        elif file.endswith('.pdf'):
            shutil.move(filepath, '/home/kelechi/Downloads/PDFs')
        elif file.endswith('.zip') or file.endswith('z'):
            shutil.move(filepath, '/home/kelechi/Downloads/zipfiles')
        elif file.endswith('.rpm'):
            shutil.move(filepath, '/home/kelechi/Downloads/rpm')
        elif file.endswith('.gif') or file.endswith('.svg'):
            shutil.move(filepath, '/home/kelechi/Downloads/gifs')
            
checkfile()




# def checkfile():
#     file_types = {
#         '.txt': 'textfiles',
#         '.jpg': 'Images',
#         '.png': 'Images',
#         '.pdf': 'PDFs',
#         '.zip': 'zipfiles',
#         '.rpm': 'rpm',
#     }

#     for file in download_files:
#         filepath = os.path.join(downloads_folder, file)
#         extension = os.path.splitext(file)[1]

#         destination_folder = file_types.get(extension, 'others')
#         destination_path = os.path.join(downloads_folder, destination_folder)

#         shutil.move(filepath, destination_path)

# checkfile()
