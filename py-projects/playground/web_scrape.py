import bs4, requests, webbrowser
from selenium import webdriver

anime = ['Jigokuraku', 'Jujutsu Kaisen', 'Attack on Titan']

browser = webdriver.Firefox()
# print("ChromeDriver Version:", browser.capabilities['chrome']['chromedriverVersion'])
# browser.quit()
browser.get('http://inventwithpython.com')

clickable = browser.find_element("link text", "Blog")
print(type(clickable))

clickable.click()

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