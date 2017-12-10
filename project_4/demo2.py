from flask import Flask, Response, request
import json
from io import BytesIO
from PIL import Image
app = Flask(__name__)

@app.route("/resize", methods=["POST"])
def resize():
    scale = (request.args.get('scale'))
    # check = request.files['data'].read()
    check =request.data
    print(type(check))
    f = BytesIO(check)
    print(f)
    im = Image.open(f)
    im_type = im.format
    im.show()
    width, height = im.size
    new_w=int(width*s)
    new_h=int(height*s)
    print(str(width)+'----------'+str(height))
    ri= im.resize((new_w,new_h),Image.ANTIALIAS)
    b=BytesIO()
    new=ri.save(b,format=im_type)
    new=b.getvalue()
    test = Image.open(BytesIO(new))
    nw,nh=test.size
    print(str(nw)+'============='+str(nh))
    return new

    # new=ri.save(BytesIO(ri).read(),format=im_type)
    # print(type(new))

    # print(type(BytesIO(data)))
    # return data.flush()
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8888
    )
