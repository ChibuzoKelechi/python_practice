#! /usr/bin/env python3
# textractor.py : Uses regex to search and extract specified text

import re, pyperclip

input_text = pyperclip.paste()
text = input('Search for...  ')

pattern =  re.compile(rf'{text}', re.IGNORECASE)
search_text = pattern.findall(input_text)
match_num = len(search_text)

appear = f'{match_num} occurences'

print(appear)
print('Copied to clipboard! :)')