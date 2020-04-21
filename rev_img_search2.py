"""Use google reverse image search to look for bulbapedia page"""
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import post
from selenium.common.exceptions import NoSuchElementException

# reverse image search code
IMG_PATH = 'result.png'
SEARCH_URL = 'http://www.google.com/searchbyimage/upload'
MULTIPART = {'encoded_image': (IMG_PATH, open(IMG_PATH, 'rb')), 'image_content': ''}
RESPONSE = post(SEARCH_URL, files=MULTIPART, allow_redirects=False)

#print(RESPONSE.headers['Location'])

# open image search link and save html on first two pages
PAGE_FOUND = False
BROWSER = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')
BROWSER.get(RESPONSE.headers['Location'])
while not PAGE_FOUND:
    HTML = BROWSER.page_source
    HTML = BeautifulSoup(HTML, 'html.parser')
    RESULTS = HTML.find_all('div', 'r')
    for r in RESULTS:
        link = r.find('a', href = True)
        link = link['href']
        if link != '' and "bulbapedia" in link and not 'List_of_' in link:
            PAGE_FOUND = True
            CLIPBOARD = open('clipboard.txt', 'w')
            CLIPBOARD.write('p!catch ' + link[40:link.find('(')-1])
            print('Pokemon found')
    if not PAGE_FOUND:
        try:
            NEXT = BROWSER.find_element_by_link_text('Next')
            NEXT.click()
        except NoSuchElementException:
            print('Could not find the name of this pokemon')
            break
BROWSER.quit()
