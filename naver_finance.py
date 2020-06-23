import urllib.request as req
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
lis = soup.select('#siselist_tab_0 > tr')

def ext_name(*args):
    # i = 1
    arr = []
    for li in lis:
        if li.find('a') is not None:
            arr.append(li.select_one(*args).text)
        #     i += 1
    return arr

def result():
    results = ext_name('.tltle')
    for i, result in enumerate(results, 1):
        print(i, result)

result()