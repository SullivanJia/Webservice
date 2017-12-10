import requests
import json
# headers = {"Authorization": "token 9fa0ce7915e3b8b4de371e564b1e97bdbbad8205"}
# user = requests.Session().get('https://api.github.com/user', headers=headers).json()
class Client:

    def __init__(self, github_token):
        try:
            Client.headers={"Authorization": "token "+str(github_token),"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
            Client.user = requests.get('https://api.github.com/user', headers=Client.headers).json()
            Client.username=Client.user['login']
        except Exception as e:
            raise Exception("invalid credentials")


    def list_stars(self):
        try:
            list_starred=requests.get('https://api.github.com/user/starred',headers=Client.headers).json()
            return json.dumps(list_starred)
        except Exception as e:
            raise Exception("unknown error")
        

    def list_followers(self):
        try:
            list_followers=requests.get('https://api.github.com/users/'+str(Client.username)+'/followers',headers=Client.headers).json()
            return json.dumps(list_followers)
        except Exception as e:
            raise Exception("unknown error")
       


    def list_repo(self):
        try:
            list_repo=requests.get('https://api.github.com/user/repos',headers=Client.headers).json()
            return json.dumps(list_repo)
        except Exception as e:
            raise Exception("unknown error")


    def star_repo(self, repo_id):
        try:
            owner=requests.get('https://api.github.com/repositories/'+str(repo_id),headers=Client.headers).json()['full_name']
            starred_repo=requests.put('https://api.github.com/user/starred/'+owner,headers=Client.headers)
        except Exception as e:
            raise Exception("an error has occurred")
        
        if starred_repo.status_code == 204 :
            return json.dumps({"status": "ok"})
        else:
            raise Exception("unknown error")
       

    def follow_user(self, user_id):
        try:
            f_user=requests.get('https://api.github.com/user/'+str(user_id),headers=Client.headers).json()
            # print(f_user)
            follow_user=requests.put('https://api.github.com/user/following/'+f_user['login'],headers=Client.headers)
        except Exception as e:
            raise Exception("an error has occurred")

        if follow_user.status_code == 204 :
            return json.dumps({"status": "ok"})
        else:
            raise Exception("unknown error")
       

    def unfollow_user(self, user_id):
        
        try:
            f_user=requests.get('https://api.github.com/user/'+str(user_id),headers=Client.headers).json()
            unfollow_user=requests.delete('https://api.github.com/user/following/'+f_user['login'],headers=Client.headers)
        except Exception as e:
            raise Exception("an error has occurred")

        if unfollow_user.status_code == 204 :
            return  json.dumps({"status": "ok"})
        else :
            raise Exception("unknown error")

    def create_repo(self, name):
        try:
            repo = {'name': str(name)}
            create = requests.post('https://api.github.com/user/repos',headers=Client.headers,json=repo)
        except Exception as e:
           raise Exception("an error has occurred")
        if create.status_code == 201:
            return create.text
        else:
            raise Exception("unknown error")

    def delete_repo(self, repo_id):
        try:
            owner=requests.get('https://api.github.com/repositories/'+str(repo_id),headers=Client.headers).json()['full_name']
            delete= requests.delete('https://api.github.com/user/repos/'+owner,headers=Client.headers)
        except Exception as e:
           raise Exception("an error has occurred")
        if delete.status_code == 204:
            return json.dumps({"status": "ok"})
        else:
            raise Exception("unknown error")
