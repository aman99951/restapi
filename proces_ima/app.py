import base64
import io

from flask import Flask,render_template,request,redirect,url_for,flash
from werkzeug.utils import secure_filename
import os
from PIL import Image
import secrets
from task import *


app=Flask(__name__)
app.config['IMAGE_UPLOADS']="\\Users\\91988\\PycharmProjects\\assignPro\\proces_ima\\static\\images"

filename=''
@app.route("/",methods=['GET','POST'])
def upload_image():
   if request.method=="POST":
       image=request.files['file']
       if image.filename =='':
           print("Image must have a file name")
           return redirect(request.url)
       filename=secure_filename(image.filename)

       basedir=os.path.abspath(os.path.dirname(__file__))
       image.save(os.path.join(basedir,app.config["IMAGE_UPLOADS"],filename))

       img=Image.open(app.config["IMAGE_UPLOADS"]+"/"+filename)
       data=io.BytesIO()
       img.save(data,"JPEG")

       encode_img_data=base64.b64encode(data.getvalue())
       return render_template("main.html",filename=encode_img_data.decode("UTF-8"))
   return render_template("main.html")
app.run()