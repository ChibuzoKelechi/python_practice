#! /usr/bin/env python3
#wikipedia_search.py : program that searches Wikipedia for prompt text

import webbrowser

search_term = input('Search Wikipedia/Google for? ')

def wikisearch(keyword):
    print('Googling....Checking Wikipedia....')
    wikilink = f'https://en.wikipedia.org/wiki/{keyword}'
    googlelink = f'https://www.google.com/search?q={keyword}'
    webbrowser.open(googlelink)
    webbrowser.open_new_tab(wikilink)

wikisearch(search_term)