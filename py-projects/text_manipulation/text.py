#! python3
#! /usr/bin/python3

import pyperclip

copied_text = pyperclip.paste()

list_text = copied_text.split('\n')

mod_text = ', '.join(list_text)
copied_text = mod_text
pyperclip.copy(copied_text)
print(copied_text)



'''
text = pyperclip.paste()
print(text)

# text_array = text.split('/n')
list(text)
list_text = '_'.join(text)
mod_text = text.upper()

text = f'{mod_text} {list_text}'

pyperclip.copy(text)
print(text)
'''
