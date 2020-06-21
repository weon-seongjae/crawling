import urllib.request as dw

# imgUrl = 'http://blogfiles.naver.net/20141124_60/cuhouse1_1416840327518cYWgm_JPEG/04.jpg'
html_url = 'http://google.com'

# save_path = './img/test.jpg'
save_path2 = 'index.html'

# dw.request.urlretrieve(imgUrl, save_path)
dw.urlretrieve(html_url, save_path2)

print('다운로드 완료')