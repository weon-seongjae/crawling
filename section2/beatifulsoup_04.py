# https://www.w3schools.com/cssref/css_selectors.asp
# https://www.w3schools.com/cssref/trysel.asp

from bs4 import BeautifulSoup
import re # regex

html = '''
<html>
    <body>
        <ul>
            <li><a id = 'naver' href='http://www.naver.com'>naver</a></li>
            <li><a href='http://www.daum.net'>daum</a></li>
            <li><a href='http://www.daum.com'>daum</a></li>
            <li><a href='https://www.google.com'>google</a></li>
            <li><a href='https://www.tistory.com'>tistory</a></li>
        </ul>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# test = soup.find('a', string = 'naver')
# print(soup.find(id='naver').string)
lis = soup.find_all(href=re.compile(r'da'))

for li in lis:
    print(li.attrs['href'])
