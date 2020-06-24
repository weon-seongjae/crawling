import requests

'''
Rest : RestFul, Rest Api - POST, GET, PUT : UPDATE, REPLACE (FETCH : UPDATE, MODIFY), DELETE
http uri를 가져와서 : URI(Uniform Resource Identifier, 유알아이) 또는 통합 자원 식별자는 인터넷에 있는 자원을 나타내는 유일한 주소
Resource : 위치 명시
Method : 명시

get, post, put(fetch), delete : URI 분석

xml, json, rss 등의 형식으로 받아옴

실습과제 : https://www.apistore.co.kr/api/apiList.do
'''

payload1 = {'key1': 'value1', 'key2': 'value2'}  # dict 형태
payload2 = (('key1', 'value1'), ('key2', 'value2'))  # tuple 형태
payload3 = {'some': 'nice'}  # json 형태

# r = requests.put('http://httpbin.org/put', data=payload1)
# print(r.text)

# r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
# print(r.text)

r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
