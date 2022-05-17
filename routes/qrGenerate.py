from flask import Flask, send_file, request
from flask_restful import Resource
import random
import io
import os
import pyqrcode
import base64



class QrCreating(Resource):
    
    def post(self):

        try:
            data = request.args.get('code')
            
            ra = random.randint(1, 1000)
            name = f"any{ra}.png"
            qr=pyqrcode.create(data)
            qr.png(name,scale=8)     
            
            return_data = io.BytesIO()
            with open(name, 'rb') as fo:
                return_data.write(base64.b64encode(fo.read()))  #converting to base64
                return_data.seek(0)  
            os.remove(name)
            return send_file(return_data,as_attachment=True,mimetype='image/png',
                     attachment_filename='download_filename.png')

        except Exception as e:
          print(e)
          return {"message": "Something went wrong"}

     

