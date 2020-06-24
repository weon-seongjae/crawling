import errno
import urllib.request as req
import urllib.parse as rep
from bs4 import BeautifulSoup
import os

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# srch = input('찾을 이름을 입력하세요.' )
add_url = rep.quote_plus('아이유')
url = base_url + add_url
res = req.urlopen(url)
save_path = './img/'

try:
    if not (os.path.isdir(save_path)):
        os.makedirs(os.path.join(save_path))
except OSError as e:
    if e.errno != errno.EEXIST:
        print('폴더 만들기 실패')
        raise


soup = BeautifulSoup(res, 'html.parser')
img_lis = soup.select('div.img_area > a.thumb._thumb > img')
for i, li in enumerate(img_lis, 1):
    full_file_name = os.path.join(save_path, str(i)+'.jpg')
    req.urlretrieve(li.get('data-source'), full_file_name)

print('다운로드 완료')