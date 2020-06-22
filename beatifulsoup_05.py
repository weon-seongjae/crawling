# https://www.w3schools.com/cssref/css_selectors.asp
# https://www.w3schools.com/cssref/trysel.asp

from bs4 import BeautifulSoup

fp = open('food-list.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
# print(soup)
print("1", soup.select("li:nth-of-type(4)")[1].string)
print('2', soup.select_one('#ac-list > li:nth-of-type(4)').string)
print('3', soup.select('#ac-list > li[data-lo=\'cn\']')[0].string)
print('4', soup.select('#ac-list > li.alcohol.high')[0].string)

param = {'data-lo' : 'cn', 'class' : 'alcohol high'}
print('5', soup.find('li', param).string)
print('6', soup.find(id='ac-list').find('li', param).string)

for ac in soup.find_all('li'):
    if ac['class'] == 'alcohol high':
        print('class == alcohol high', ac.string)

# fnd = soup.select('div > ul#ac-list > li')[3]
# print(fnd.text)