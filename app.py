import os
from flask import Flask, send_from_directory
from flask_restful import Api
from routes.icoRoute import IcoConverter 
from routes.pngToJpg import PngToJpg
from routes.pngToJpeg import PngToJpeg
from routes.jpgToPng import JpgToPng
from routes.jpgToJpeg import JpgToJpeg
from routes.jpegToPng import JpegToPng
from routes.jpegToJpg import JpegToJpg
from routes.resizeImage import ResizeImage
from routes.qrGenerate import QrCreating
from routes.qrDecode import QrDecode
from routes.shortLink import ShortLink
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route("/", methods=['GET'])
def home():
    return {"message": "This is initial route"}

api.add_resource(IcoConverter,"/ico")
api.add_resource(PngToJpg,"/pngtojpg")
api.add_resource(JpgToPng, "/jpgtopng")
api.add_resource(PngToJpeg, "/pngtojpeg")
api.add_resource(JpgToJpeg, "/jpgtojpeg")
api.add_resource(JpegToPng, "/jpegtopng")
api.add_resource(JpegToJpg, "/jpegtojpg")
api.add_resource(ResizeImage, "/resizeimage")
api.add_resource(QrCreating,"/qrcreation")
api.add_resource(QrDecode, "/qrdecode")
api.add_resource(ShortLink, "/shortlink")


if __name__ == "__main__":
    app.run(port="5000", debug=True, host='0.0.0.0')