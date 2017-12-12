import sqlite3
from flask import Flask, Response
from flask_jsonrpc import JSONRPC
import json
import requests


app = Flask(__name__)

jsonrpc = JSONRPC(app, '/')

@jsonrpc.method('sql_con')
def sql_con():
    print("client connected")
    con = sqlite3.connect('testdb.db')
    cs = con.cursor()
    rs = cs.execute('SELECT * FROM student_table;')
    result = ""
    for row in rs:
        result = result + row[0] + '\n'
    # print(result)
    data= {
        "result": result
        }
    format = json.dumps(data)
    # print(json.dumps(data))
    return Response(
            response=format,
            mimetype="application/json",
            status=200
        )
    con.close()

def register_service():
    data = {
        "ID": "redis1",
        "Name": "redis",
        "Address": "172.26.114.120",
        "Port": 8001}

    try:
        response = requests.put(
        "http://172.26.114.120:8500/v1/agent/service/register",
        data=str(json.dumps(data))
        )
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        raise("can not find consul")
    



if __name__ == '__main__':
    if register_service():
        print("Connected consul")
        app.run(
        host='0.0.0.0',
        port=8001)
    else:
        print("can not register")

