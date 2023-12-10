from operator import index
import re

# nm_pt = re.compile(r'.')
pw_pattern = re.compile(r'\d\d\d\d')
# widePt = re.compile(r'midnight (.*)')
# py_pt = re.compile(r".*?\.py")
offense_pt = re.compile(r'.*[fuck]+')


test_string = "The code is k-1735, not k-7207"
n_words = 'yo, nigga, fuck off. Get the fuck out, fuck it'
name = "Night is the best time for fight, midnight for code"
file_names = "In my home folder, i have win.py, passkey.py, and test.py files"


pw_pattern.sub('****', test_string)
check_lang = offense_pt.search(n_words)
subpt = pw_pattern.sub('****', test_string)

print(subpt)

# for match in inpattern:
#     print(match)

# for match in checkpy:
#     print(match)
