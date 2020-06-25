import requests, json

'''
Rest : RestFul, Rest Api
http uri를 가져와서 : URI(Uniform Resource Identifier, 유알아이) 또는 통합 자원 식별자는 인터넷에 있는 자원을 나타내는 유일한 주소
Resource : 위치 명시
Method : 명시

get, post, put(fetch), delete : URI 분석

xml, json, rss 등의 형식으로 받아옴

실습과제 : https://www.apistore.co.kr/api/apiList.do
'''

# r = requests.get('https://api.github.com/events')
# r.raise_for_status()
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org', path='/cookies')

# r = requests.get('http://httpbin.org/cookies', cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com', timeout=3)
# print(r.text)

# r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
# print(r.text)

payload1 = {'key1' : 'value1', 'key2' : 'value2'} # dict 형태
payload2 = (('key1', 'value1'), ('key2', 'value2'))  # tuple 형태
payload3 = {'some': 'nice'}  # json 형태

# r = requests.post('http://httpbin.org/post', data=payload1) # form으로 전송
# print(r.text)

r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) # json으로 전송
print(r.text)


