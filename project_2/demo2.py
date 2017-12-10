# from flask_jsonrpc.proxy import ServiceProxy
# import json
# c = ServiceProxy('http://127.0.0.1:3000/')
# print(c.time())
# print(c.ram())
# print(c.hdd())
# print(c.add(2,3))
# print(c.sub(1,3))
# print(c.json_to_xml('{"message":"I am a JSON message"}'))

from http_rpc_client import Client

c = Client("127.0.0.1:3000")

# print(c.time())
# print(c.ram())
# print(c.hdd())
# print(c.add(2,3))
# print(c.sub(1,3))
print(c.json_to_xml('{"message":"I am a JSON message"}'))