# https://www.w3schools.com/cssref/css_selectors.asp
# https://www.w3schools.com/cssref/trysel.asp

from bs4 import BeautifulSoup

fp = open('food-list.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
# print(soup)
print("1", soup.select_one("li:nth-of-type(5)"))

# fnd = soup.select('div > ul#ac-list > li')[3]
# print(fnd.text)