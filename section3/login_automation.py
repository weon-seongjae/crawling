import requests
from bs4 import BeautifulSoup
import re

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
    'user_id': 'weonsj',
    'user_pw': 'wsj0707!@#'
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    # HTML 소스 확인
    # print('login_req', login_req.text)
    # Header 확인
    # print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://bbs.ruliweb.com/market/board/32/read/4737038')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        articles = soup.select('div.col_12.text_center')[2].select('div.col')[1]
        article = articles.text
        chg = re.sub(r'\s{2,}', '\n', article, re.U)
        chg = re.sub(r'(\. *)(우.+?$)','\1\n\2', chg, re.U, re.M)
        print(chg.strip())
