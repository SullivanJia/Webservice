import requests
import json
headers = {"Authorization": "token 9fa0ce7915e3b8b4de371e564b1e97bdbbad8205",'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}
user = requests.Session().get('https://api.github.com/user', headers=headers).json()
repo = {
  "name": "newWorld2"
}
create = requests.post('https://api.github.com/user/repos',headers=headers,json=repo)#创建仓库
print(create)
print(type(create.text))
print(type(create))

# delete= requests.delete('https://api.github.com/user/repos/'+'id')#删除用户
# l_starred= requests.get('https://api.github.com/user/starred',headers=headers)#加星标
# starred_repo=requests.put('https://api.github.com/user/starred/'+'id',headers=headers)
# username=user['login']	
# list_follow=requests.get('https://api.github.com/users/'+username+'/followers',headers=headers)
# follwers=requests.get('https://api.github.com/users/SullivanJia/followers',headers=headers)# 查看用户关注人
# list_repo=requests.get('https://api.github.com/repositories/109506165',headers=headers)#查看用户的仓库列表
#owner=requests.get('https://api.github.com/user/26838155',headers=headers).json()
# starred_repo=requests.put('https://api.github.com/user/starred/'+owner,headers=headers)
# follow=requests.put('https://api.github.com/user/following/'+username,headers=headers)#关注他人
# unfollow=requests.delete('https://api.github.com/user/following/'+username,headers=headers)#取消关注他人
# def star_repo(repo_id):
#         try:
#             owner=requests.get('https://api.github.com/repositories/'+str(repo_id),headers=headers).json()['full_name']
#             starred_repo=requests.put('https://api.github.com/user/starred/'+owner,headers=headers)
#         except Exception as e:
#             raise Exception("an error has occurred")
        
#         if starred_repo.status_code == 204 :
#             return  {"status": "ok"}
#         else:
#             raise Exception("unknown error")

# print(star_repo(109506165))


