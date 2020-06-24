import urllib.request as req
# import urllib.parse as rep
from bs4 import BeautifulSoup

url = 'https://www.inflearn.com/'
# quote = rep.quote_plus('추천-강좌')
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')

lis = soup.find_all('.swiper-container.five welcome.swiper-container-initialized.swiper-container-horizontal')
print(lis)
# for li in lis:
#     item = li.select_one('.course_title')
#     print(item.string)
# for i, li in enumerate(lis, 1):
#     print(i, li.text)
