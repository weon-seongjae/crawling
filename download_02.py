import urllib.request as dw

img_url = 'http://blogfiles.naver.net/20141124_60/cuhouse1_1416840327518cYWgm_JPEG/04.jpg'
html_url = 'http://google.com'

save_path1 = './img/test.jpg'
save_path2 = 'index.html'

f = dw.urlopen(img_url).read()
f2 = dw.urlopen(html_url).read()

save_file1 = open(save_path1, 'wb') # w : write, r : read, a : append
save_file1.write(f)
save_file1.close()

with open(save_path2, 'wb') as save_file2:
    save_file2.write(f2)

print('다운로드 완료')