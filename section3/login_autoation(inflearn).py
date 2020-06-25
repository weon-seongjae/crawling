import requests

'''
Rest : RestFul, Rest Api - POST, GET, PUT : UPDATE, REPLACE (FETCH : UPDATE, MODIFY), DELETE
http uri를 가져와서 : URI(Uniform Resource Identifier, 유알아이) 또는 통합 자원 식별자는 인터넷에 있는 자원을 나타내는 유일한 주소
Resource : 위치 명시
Method : 명시

get, post, put(fetch), delete : URI 분석

xml, json, rss 등의 형식으로 받아옴

실습과제 : https://www.apistore.co.kr/api/apiList.do

http://docs.python-requests.org/en/master/user/advanced
'''

# 로그인 유저 정보
LOGIN_INFO = {
    'email': 'weonsj@gmail.com',
    'password': 'wsj461631',
}

with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/api/signin', data=LOGIN_INFO)
    # html 소스확인
    # print('login_req'.format(login_req.text))
    # html 헤더 확인
    # print('login_req'.format(login_req.headers))
    if login_req.status_code == 200 and login_req.ok:
        dash_info = s.get('https://www.inflearn.com/dashboard')
        dash_info.raise_for_status()
        print(dash_info.text)
    # if login_req.status_code == 200 and login_req.ok:
    #     post_one = s.get('https://www.inflearn.com/messages')
    #     post_one.raise_for_status()
    #     soup = BeautifulSoup(post_one.text, 'html.parser')
    #     print(soup.prettify())
