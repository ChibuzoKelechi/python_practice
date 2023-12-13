#! /usr/bin/env python3
#wikipedia_search.py : program that searches Wikipedia for prompt text

import webbrowser

search_term = input('Search Wikipedia for? ')

def wikisearch(keyword):
    print('Googling....Checking Wikipedia....')
    search_link = f'https://en.wikipedia.org/wiki/{keyword}'
    webbrowser.open(search_link)

wikisearch(search_term)