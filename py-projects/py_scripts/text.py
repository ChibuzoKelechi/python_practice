#! /usr/bin/env python3
# text.py: turns copied lists into one line statements(with comma/colon separation)

import pyperclip

copied_text = pyperclip.paste()

list_text = copied_text.split('\n')

mod_text = '; '.join(list_text)

copied_text = mod_text
pyperclip.copy(copied_text)
print(mod_text)