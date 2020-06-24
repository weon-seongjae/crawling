from urllib.parse import urljoin
# baseUrl = 'http://test.com/html/a.html'
# print('>>', urljoin(baseUrl, 'b.html'))
# print('>>', urljoin(baseUrl, 'sub/b.html'))
# print('>>', urljoin(baseUrl, '../index.html'))
# print('>>', urljoin(baseUrl, '../img/img.jpg'))
# print('>>', urljoin(baseUrl, '../css/img.css'))

from bs4 import BeautifulSoup
import sys, io

html = '''
<html>
    <body>
        <ul>
            <li><a href='http://www.naver.com'>naver</a></li>
            <li><a href='http://www.daum.net'>daum</a></li>
            <li><a href='http://www.daum.com'>daum</a></li>
            <li><a href='https://www.google.com'>google</a></li>
            <li><a href='https://www.tistory.com'>tistory</a></li>
        </ul>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
# print('links', type(links))

# for a in links:
#     # print('a', type(a), a)
#     href = a.attrs['href']
#     txt = a.string
#     print(txt)

# links = soup.select('li > a')
# for link in links:
#     print(link.text, link.get('href'))

# a = soup.find_all('a', string='daum')
# print('a', a)
# b = soup.find_all('a', limit=0)
# print('b', b)

# c = soup.find_all(string=['naver', 'google'])
# print('c', c)

