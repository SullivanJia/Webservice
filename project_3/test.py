from github_client import Client
import json
c=Client('9fa0ce7915e3b8b4de371e564b1e97bdbbad8205')
print(c.list_stars())
print(c.list_followers())
print(c.list_repo())
print(c.star_repo(112074598))
print(c.follow_user(16163498))
print(c.create_repo('test6'))

