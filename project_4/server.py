from flask import Flask, Response, request
from io import BytesIO
from PIL import Image
app = Flask(__name__)
@app.route("/resize", methods=["POST"])
def resize():
    try:
        scale = request.values.get('scale')
        get_float=float(scale)
        check = request.files['data'].read()
        im = Image.open(BytesIO(check))
        width, height = im.size
        im_type = im.format
        ri = im.resize((int(width * get_float), int(height * get_float)))
        data = BytesIO()
        ri.save(data,im_type)
    except Exception as e:
        return Response(status=400)
    else:
        return data.getvalue()
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8888
    )
