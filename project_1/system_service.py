from flask import Flask,Response
import json
import time
import psutil
app = Flask(__name__)

@app.route("/time", methods=["GET"])
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

@app.route("/ram", methods=["GET"])
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

@app.route("/hdd", methods=["GET"])
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



if __name__ == '__main__':
    app.run(
        port=3000
    )
