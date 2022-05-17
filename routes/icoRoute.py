from flask import request, send_file
from flask_restful import Resource
import imageio as iio
import io
import random
import base64
import os

class IcoConverter(Resource):
    def post(self):
        
        try:

            image_data = request.get_data()
            im = iio.imread(image_data)
            ra = random.randint(1,111)
            name = f"logo{ra}.ico"
            imgs=iio.imwrite(name, im)
            return_data = io.BytesIO()
            with open(name, 'rb') as fo:
                return_data.write(base64.b64encode(fo.read()))
                return_data.seek(0)  
            os.remove(name)
            return send_file(return_data, as_attachment=True, mimetype="image/x-icon",
                     attachment_filename='download_filename.ico')

          
        except Exception as e:
            print(e)
            return {"message": "Something went wrong"}
        
      
       