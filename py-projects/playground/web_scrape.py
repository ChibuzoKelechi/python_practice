import bs4, requests, webbrowser

# webbrowser.open('kaggle.com')
# target_site = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# res = requests.get(target_site)
# res.raise_for_status()
# py_wiki = bs4.BeautifulSoup(res.text)

# print(type(py_wiki))

search_term = input('Search for: ')
def google(keyword):
    print('Googling....Checking Wikipedia....')
    search_link = f'https://en.wikipedia.org/wiki/{keyword}'
    webbrowser.open(search_link)

google(search_term)




# try:
#     res.raise_for_status
#     print('Success')
#     webbrowser.open(target_site)
# except Exception as exc:
#     print('There was an error: %s' % (exc))