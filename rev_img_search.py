"""Use google reverse image search to look for bulbapedia page"""
from bs4 import BeautifulSoup
from selenium import webdriver
from requests import post

# reverse image search code
IMG_PATH = 'result.png'
SEARCH_URL = 'http://www.google.com/searchbyimage/upload'
MULTIPART = {'encoded_image': (IMG_PATH, open(IMG_PATH, 'rb')), 'image_content': ''}
RESPONSE = post(SEARCH_URL, files=MULTIPART, allow_redirects=False)

#print(RESPONSE.headers['Location'])

# open image search link and save html on first two pages
BROWSER = webdriver.Chrome(executable_path='./chromedriver_win32/chromedriver.exe')
BROWSER.get(RESPONSE.headers['Location'])
HTML = BROWSER.page_source
HTML_P1 = BeautifulSoup(HTML, 'html.parser')
#NEXT = HTML_P1.find('a', 'G0iuSb')
NEXT = BROWSER.find_element_by_link_text('Next')
NEXT.click()
HTML = BROWSER.page_source
HTML_P2 = BeautifulSoup(HTML, 'html.parser')
BROWSER.quit()

# gather results and print links with bulbapedia in them to clipboard
DIVS = HTML_P1.find_all('div', 'r')
DIVS = DIVS + HTML_P2.find_all('div', 'r')

print('Links found')

LINKS = []
for r in DIVS:
    try:
        link = r.find('a', href = True)
        if link != '':
            LINKS.append(link['href'])
    except:
        continue

for l in LINKS:
    if "bulbapedia" in l and not 'List_of_' in l:
        CLIPBOARD = open('clipboard.txt', 'w')
        CLIPBOARD.write('p!catch ' + l[40:l.find('(')-1])