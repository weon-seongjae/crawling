import urllib.request as req
from urllib.parse import urlencode

url1 = 'https://ssl.pstatic.net/tveta/libs/1281/1281529/8160fccfed65bee565f3_20200619145636845.jpg'
url2 = 'https://ssl.pstatic.net/tveta/libs/1291/1291857/5c3396f4d37a70aa040f_20200610135851603.jpg'

save1 = './img/top.jpg'
save2 = './img/right.jpg'
rd1 = req.urlopen(url1).read()
rd2 = req.urlopen(url2).read()
with open(save1, 'wb') as f:
    f.write(rd1)
with open(save2, 'wb') as g:
    g.write(rd2)
