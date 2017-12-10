import requests
import json
params={'scale' : 2,'data': '/Users/jiaguanyi/Desktop/WX20171111-003553.png'}
get_data = requests.post('http://127.0.0.1:3000/resize',params=params)
print(get_data.url)
print(type(get_data.text))


