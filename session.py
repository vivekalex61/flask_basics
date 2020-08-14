from flask import Flask ,render_template,request,session ,redirect ,url_for,abort


app=Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')

def log():
      if 'username' in session:
           username = session['username']
           return 'Logged in as ' + username + '<br>' + \
           "<b><a href = '/logout'>click here to log out</a></b>"
      else: 
         return '<html><body><form action = "http://localhost:5000/login" method = "post"><p>Enter Name:</p><p><input type = "text" name = "nm" /></p><p><input type = "submit" value = "submit" /></p></form></body></html>'
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
           
      session['username'] = request.form['nm']
      if session['username']=='admin' :
         

         return redirect(url_for('index'))
      else:
         
         abort(401)      
   
@app.route('/ind')
def index():
   return 'Logged in as ' + session['username'] + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"

@app.route('/logout')
def logout():
   #for removing the username in session
   session.pop('username', None)
   return redirect(url_for('log'))

   


if __name__ == '__main__':
   app.run(debug = True)
