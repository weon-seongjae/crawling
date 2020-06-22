# https://www.w3schools.com/cssref/css_selectors.asp
# https://www.w3schools.com/cssref/trysel.asp

from bs4 import BeautifulSoup

fp = open('cars.html', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')

def car_func(selector):
    print('car_func', soup.select_one(selector).string)

car_lambda = lambda q : print('car_lambda', soup.select_one(q).string)

car_func('#gr')
car_func('li#gr')
car_func('ul > li#gr')
car_func('#cars #gr')
car_func('li:nth-of-type(4)')
car_func('li[id=\'gr\']')

car_lambda('#gr')
car_lambda('li#gr')
car_lambda('ul > li#gr')
car_lambda('#cars #gr')
car_lambda('li:nth-of-type(4)')
car_lambda('li[id=\'gr\']')

print(soup.select('li')[3].string)
print('car_funt', soup.find_all('li')[3].string)