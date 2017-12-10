import requests
import json
headers = {"Authorization": "token 9fa0ce7915e3b8b4de371e564b1e97bdbbad8205"}
user = requests.Session().get('https://api.github.com/user', headers=headers).json()
# repo = {
#   "name": "newWorld"
# }
# create = requests.post('https://api.github.com/user/repos',headers=headers,json=repo)#创建仓库
# delete= requests.delete('https://api.github.com/user/repos/'+'id')#删除用户
# l_starred= requests.get('https://api.github.com/user/starred',headers=headers)#加星标
# starred_repo=requests.put('https://api.github.com/user/starred/'+'id',headers=headers)
# username=user['login']	
# list_follow=requests.get('https://api.github.com/users/'+username+'/followers',headers=headers)
# follwers=requests.get('https://api.github.com/users/SullivanJia/followers',headers=headers)# 查看用户关注人
list_repo=requests.get('https://api.github.com/user/repos',headers=headers)#查看用户的仓库列表
# follow=requests.put('https://api.github.com/user/following/'+username,headers=headers)#关注他人
# unfollow=requests.delete('https://api.github.com/user/following/'+username,headers=headers)#取消关注他人

print(list_repo.text)

