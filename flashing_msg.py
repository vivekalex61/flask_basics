from flask import Flask ,render_template,request,session ,redirect ,url_for,abort,flash


app=Flask(__name__)
app.secret_key = 'any random string'



@app.route('/')
def index():
   return render_template('index_for_flash_message.html')

@app.route('/login', methods = ['GET', 'POST'])

def login():
   error = None
   
   if request.method == 'POST':
      if request.form['nm'] != 'admin':

        error = 'Invalid username or password. Please try again!'
       
      else:
         flash('You were successfully logged in')
         return redirect(url_for('index'))
    return render_template('loginn.html', error = error)  
    


   


if __name__ == '__main__':
   app.run(debug = True)
