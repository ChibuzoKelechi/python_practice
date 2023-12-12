import os, cv2

t_file = 'py-projects/playground/me.txt'
blank = 'py-projects/playground/blank.txt'
file_size = os.path.getsize(t_file)
subdirs = os.listdir('py-projects/playground')

print(f'{file_size} bytes')

txtfile = open('py-projects/playground/me.txt', 'r')
blankfile = open('py-projects/playground/blank.txt', 'w+')

blankfile.write('''Python
 Scikit-Learn:
 Familiarize yourself with the Scikit-Learn library for machine learning algorithms, \n data preprocessing, and model evaluation.
                            ''')
# blankfile.close()
filecont = blankfile.read()

# print(filecont)



# totalsize = 0
# for dir in subdirs:
#     totalsize += os.path.getsize(os.path.join('py-projects/playground', dir))
#     print(dir)
# print(f'Total size of this directory is {totalsize} bytes')
#  print(dir(cv2))
# shutil.copy('py-projects/playground/me.txt', 'py-projects/text_manipulation')
# os.unlink('py-projects/text_manipulation/me.txt')