from flask import Flask,Response
from flask_jsonrpc import JSONRPC
import json
import time
import psutil
import dicttoxml

app = Flask(__name__)

jsonrpc = JSONRPC(app, '/')
@jsonrpc.method('time')
def get_time():
    t_json = {
        "time" : int(time.time())
    }
    format = json.dumps(t_json)
    return Response(
        response= format,
        mimetype="application/json",
        status=200
    )

@jsonrpc.method('ram')
def get_ram():
    r_json = {
        "total" : int((psutil.virtual_memory().total/1024)/1024),
        "used" : int((psutil.virtual_memory().used/1024)/1024)
    }
    format = json.dumps(r_json)
    return Response(
        response=format,
        mimetype="application/json",
        status=200
    )

@jsonrpc.method('hdd')
def get_hdd():
    h_json = {
        "total" : int((psutil.disk_usage('/').total/1024)/1024),
        "used" : int((psutil.disk_usage('/').used/1024)/1024)
    }
    format = json.dumps(h_json)
    return Response(
        response=format,
        mimetype="application/json",
        status=200

    )

@jsonrpc.method('add')
def add(x,y):

		return x+y



@jsonrpc.method('sub')
def sub(x,y):
	return int(x-y)


@jsonrpc.method('json_to_xml')
def json_to_xml(data):
	result=str(dicttoxml.dicttoxml(json.loads(data)),encoding="utf-8")

	jtt_json = {
		"result" : result

	}
	format = json.dumps(jtt_json)
	return Response(
		response=format,
        mimetype="application/json",
        status=200
		)



if __name__ == '__main__':
    app.run(
        port=3000
    )
