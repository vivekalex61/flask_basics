from flask import Flask, redirect, url_for, request
app = Flask(__name__)
#redirecting page
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
#getting the name forom website.html
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
       
if __name__ == '__main__':
   app.run(debug = True)
