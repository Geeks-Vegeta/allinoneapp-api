from flask import Flask, send_file, request
from flask_restful import Resource
from pyzbar.pyzbar import decode
from PIL import Image
import random
import io
import os
import base64
import codecs



class QrDecode(Resource):
    
    def post(self):

        try:
            data = request.get_data()
            d=decode(Image.open(io.BytesIO(data)))
            axi_data = d[0].data.decode('ascii')
            return {"message": f"{axi_data}"}

        except Exception as e:
          print(e)
          return {"message": "QR Image Only"},404

     

