from flask import Flask, send_file, request
from flask_restful import Resource
from PIL import Image
import random
import io
import base64
import os




class JpgToPng(Resource):
    
    def post(self):

        try:
            data = request.get_data()
            im = Image.open(io.BytesIO(data))
            rgb_im = im.convert('RGB')
            ra = random.randint(1, 1000)
            name = f"topng{ra}.png"
            rgb_im.save(name)

            return_data = io.BytesIO()
            with open(name, 'rb') as fo:
                return_data.write(base64.b64encode(fo.read()))
                return_data.seek(0)  
            os.remove(name)
            return send_file(return_data,as_attachment=True,mimetype='image/png',
                     attachment_filename='download_filename.png')

        except Exception as e:
          print(e)
          return {"message": "Something went wrong"}

     

