#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

target_url = 'https://djangoproject.com'
browse_env = webdriver.Firefox()
print('Currently in homepage..')

def screenshot_page(filename):
    browse_env.implicitly_wait(10)
    screenshot = browse_env.get_screenshot_as_png()
    print(f'Screenshot of {filename} taken')
    with open(f'{filename}.png', "wb") as f:
        f.write(screenshot)

    
def sitewalk():
    print('Walking through the site..')
    browse_env.implicitly_wait(10)
    install_guide = browse_env.find_element('link text', 'DJANGO INSTALLATION GUIDE')
    install_guide.click()
    screenshot_page('django-install')
    tutorial = browse_env.find_element('link text', 'Django at a glance')
    tutorial.click()
    screenshot_page('dj-tutorial-page')
           
        
browse_env.get(target_url)
screenshot_page('django-home')

click_start = browse_env.find_element('link text', 'Get started with Django')
click_start.click()
screenshot_page('django-intro')
        
sitewalk()
print('Enjoy your tutorial :) ')