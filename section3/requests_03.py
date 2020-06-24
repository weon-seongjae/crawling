import requests, json

# Response 상태 코드

s = requests.Session()

# https://jsonplaceholder.typicode.com

r = s.get('http://httpbin.org/stream/20', stream=True)
# print(r.text)
# print(r.encoding)

if r.encoding is None:
    r.encoding = 'utf-8'

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) # dict
    # print(b)

    for e in b.keys():
        # print(b[e])
        print('key:', e, 'value:', b[e])


