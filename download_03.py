from urllib.request import urlopen

img_url = 'http://blogfiles.naver.net/MjAxNjEwMjdfMjE1/MDAxNDc3NTMxOTAyNzg0.3q5qfvzikazXia81CeI4u5LpFIi0A7KzaBBHc0sqgo4g.YtQDOJDqvdZv7wkzgtTJiWvz-FcsACu-QRH-7EXtOVsg.JPEG.txzty2/%C3%A2%BF%F8%B0%AD%BE%C6%C1%F6%BA%D0%BE%E7%B1%A4%B8%ED%B0%AD%BE%C6%C1%F6%BA%D0%BE%E76.jpg'

html_url = 'http://google.com'
#
save_img = './img/dog1.jpg'
save_html = 'index.html'
#
# dl.urlretrieve(html_url, save_html)
#
# print('다운 완료!')

f = urlopen(img_url).read()
save_file1 = open('./img/dog1.jpg', 'wb')
# save_file1.write(f)
save_path = 'index.html'
url = urlopen(html_url).read()
with open(save_path, 'wb') as f2:
    f2.write(url)

