from operator import index
import re

# nm_pt = re.compile(r'.')
pw_pattern = re.compile(r'k-\d\d\d\d')
# widePt = re.compile(r'midnight (.*)')
# py_pt = re.compile(r".*?\.py")
offense_pt = re.compile(r'.*[fuck]+')


test_string = "The code is k-1735, not k-7207"
n_words = 'yo, nigga, fuck off. Get the fuck out, fuck it'
name = "Night is the best time for fight, midnight for code"
file_names = "In my home folder, i have win.py, passkey.py, and test.py files"

# checkPt = pw_pattern.search(test_string)
# inpattern = pw_pattern.search(test_string)
pw_pattern.sub('****', test_string)
# checkNm = nm_pt.findall(name)
# forcheck = widePt.search(name)
# check_py = py_pt.search(file_names)
# checkpy = py_pt.findall(file_names)
check_lang = offense_pt.search(n_words)

print(test_string)
# print(inpattern)
# print(checkPt.group())
# print(forcheck.group())
# print(check_py.group(0))
# print(check_lang.group())


# for match in inpattern:
#     print(match)

# for match in checkpy:
#     print(match)
