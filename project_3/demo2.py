import requests
import re

session = requests.Session()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_octo=GH1.1.1664649958.1449761838; _gat=1; logged_in=no; _gh_sess=eyJsYXN0X3dyaXRlIjoxNDcyODA4MTE1NzQ5LCJzZXNzaW9uX2lkIjoiZGU3OTQ1MWE0YjQyZmI0NmNhYjM2MzU2MWQ4NzM0N2YiLCJjb250ZXh0IjoiLyIsInNweV9yZXBvIjoiY25vZGVqcy9ub2RlY2x1YiIsInNweV9yZXBvX2F0IjoxNDcyODA3ODg0LCJyZWZlcnJhbF9jb2RlIjoiaHR0cHM6Ly9naXRodWIuY29tLyIsIl9jc3JmX3Rva2VuIjoiTllUd3lDdXNPZmtyYmRtUDdCQWtpQzZrNm1DVDhmY3FPbHJEL0U3UExGaz0iLCJmbGFzaCI6eyJkaXNjYXJkIjpbXSwiZmxhc2hlcyI6eyJhbmFseXRpY3NfbG9jYXRpb25fcXVlcnlfc3RyaXAiOiJ0cnVlIn19fQ%3D%3D--91c34b792ded05823f11c6fe8415de24aaa12482; _ga=GA1.2.1827381736.1472542826; tz=Asia%2FShanghai",
    "Host": "github.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
}


def getToken():
    html = session.get('https://github.com/login', headers=header)
    tokenPattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')
    print (html.content)
    authenticity_token = re.findall(tokenPattern,html.text)[0]
    return authenticity_token


def userpwdLogin():
    payload = {'login': 'loginname',
               'password': 'pwd',
               'commit': 'Sign+in',
               'authenticity_token': getToken(),
               'utf8': "✓"}
    r = session.post('https://github.com/session', data=payload, headers=header)
    print(r.status_code)
    print("the session rsult is: ", r.status_code)
    print("the reason is: ", r.reason)
    # print("the detail is: ", r.text)

userpwdLogin()
