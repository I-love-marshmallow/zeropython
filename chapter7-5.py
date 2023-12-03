print('7-5 Webスクレイピング')

import requests

html = requests.get('https://www.hungarymedical.org/school/semmelweis/curriculum.html?gad_source=1&gclid=Cj0KCQiAyKurBhD5ARIsALamXaFgl3Hmjc9WxDfZdi767WfUpuGwXRB4ZeID4fDgI5xLSQhsmGuZ17IaAsWcEALw_wcB')
print(html.text)

html = requests.get('https://anurseinthemaking.com/pages/about')
print(html.text)

import requests
from bs4 import BeautifulSoup 

result = requests.get('https://anurseinthemaking.com/pages/about')
soup = BeautifulSoup(result.text, 'html.parser')

for sec in soup.select('section'):
    style = sec.select_one('style')
    
    if style:
        category = style.text

        # Check if 'ul' exists within the 'section'
        ul = sec.select_one('div')
        if ul:
            # Check if 'li' exists within the 'ul'
            li = ul.select_one('li')
            if li:
                title = li.text
                print('Category:', category)
                print('Title:', title)