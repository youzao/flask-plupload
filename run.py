#coding=utf-8
from flask import Flask,render_template,url_for, session,escape,redirect
app = Flask(__name__)
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory,session,escape
from werkzeug import secure_filename
app.config['UPLOAD_FOLDER'] = '/tmp/'
@app.route('/')
def index():
     return render_template('/index.html')
@app.route('/upload.html', methods=['GET', 'POST', 'OPTIONS'])
def upload():
      filename=request.form['name']
      file=request.files['file']
      filename= filename.encode("utf-8")
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return render_template('/upload.html')

if __name__ == '__main__':
        app.run(host="0.0.0.0",port=80, debug=True)
