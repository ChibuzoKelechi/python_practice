import bs4, requests, webbrowser
from selenium import webdriver

anime = ['Jigokuraku', 'Jujutsu Kaisen', 'Attack on Titan']

browser = webdriver.Firefox()
browser.get('https://kaggle.com')

clickable = browser.find_element("link text", "Courses")

print(type(clickable))

clickable.click()

# browser.get('http://inventwithpython.com')


# webbrowser.open('kaggle.com')
# target_site = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# res = requests.get(target_site)
# res.raise_for_status()
# py_wiki = bs4.BeautifulSoup(res.text)

# browser.get('https://google.com')

# try:
#     section = browser.find_element('search')
#     print('Found <%s> element with that class name!' % (section.tag_name))
# except:
#     print('Unavailable')

# email_field = browser.find_element('id', 'identifierId')
# pwd_field = browser.find_element('id', 'password')

# email_field.send_keys('')
# pwd_field.send_keys('')
# email_field.submit()
# pwd_field.submit()

# print(type(py_wiki))

# search_term = input('Search for: ')
# def google(keyword):
#     print('Googling....Checking Wikipedia....')
#     search_link = f'https://en.wikipedia.org/wiki/{keyword}'
#     webbrowser.open(search_link)

# google(search_term)


# try:
#     res.raise_for_status
#     print('Success')
#     webbrowser.open(target_site)
# except Exception as exc:
#     print('There was an error: %s' % (exc))

# print("ChromeDriver Version:", browser.capabilities['chrome']['chromedriverVersion'])
# browser.quit()