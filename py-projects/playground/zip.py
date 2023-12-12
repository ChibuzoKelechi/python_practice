import zipfile, os

# zip_file = zipfile.ZipFile('first-python-main.zip') 

# zip_file.extractall('py-projects/testfolder')

# zip_file.close()

myzip = zipfile.ZipFile('py-projects/testfolder/me.zip', 'w')

myzip.write('py-projects/testfolder/first-python-main/first.py', compress_type=zipfile.ZIP_DEFLATED)
myzip.close()
