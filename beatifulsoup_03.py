# https://www.w3schools.com/cssref/css_selectors.asp
# https://www.w3schools.com/cssref/trysel.asp

from bs4 import BeautifulSoup

html = '''
<html>
    <body>
        <div id = 'main'>
            <h1>강의목록</h1>
            <ul class='lecs'>
                <li>Java 초고수 되기</li>
                <li>파이썬 기초 프로그래밍</li>
                <li>파이썬 머신러닝 프로그래밍</li>
                <li>안드로이드 블루투스 프로그래밍</li>
            </ul>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
lis = soup.select('div#main > ul.lecs > li')
for li in lis:
    print(li.text)
