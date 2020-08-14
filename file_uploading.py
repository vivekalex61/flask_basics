from flask import Flask ,render_template,request,session ,redirect ,url_for,abort,flash

from werkzeug.utils import secure_filename
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='/home/vivek/Desktop'
app.secret_key = 'any random string'

@app.route('/')
def index():
   return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
   


if __name__ == '__main__':
   app.run(debug = True)
