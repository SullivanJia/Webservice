import requests
import json

user = "541860829@qq.com"
pwd = "Jiaguanyi001"
r=requests.get('https://api.github.com/user', auth=(user, pwd))
print(r)
print (json.loads(r.text)['following'])
