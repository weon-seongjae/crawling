import urllib.request as req
from urllib.parse import urlparse

url = 'http://www.encar.com'

mem = req.urlopen(url)

# print(type(mem))
# print('geturl', mem.geturl())
# print('status', mem.status)
# print('headers',mem.getheaders())
# print('info', mem.info())
# print('code', mem.getcode())
# print('read', mem.read().decode('cp949'))
print(urlparse(url))