import json
import requests
from flask_jsonrpc.proxy import ServiceProxy
# 12月12号
def con_consul():
    print("Connecting to consul... [OK]")
    try:
        response = requests.get("http://172.26.114.120:8500/v1/agent/services")
        if response.status_code == 200:
            print("Looking for database... [OK]")
            return response
        else:
            print("can not connect to consul")
    except Exception as e:
        raise("ip_address is not ok ")
    

    # print(response.content)
def exe_sql(response):
    address=response.json()['redis1']['Address']
    port=response.json()['redis1']['Port']
    ip_address="http://"+str(address)+":"+str(port)+"/"
    data=ServiceProxy(ip_address).sql_con()
    print(data['result'])

if __name__ == '__main__':
    exe_sql(con_consul())