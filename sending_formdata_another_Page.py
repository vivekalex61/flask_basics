from flask import Flask ,render_template,request


app=Flask(__name__)
@app.route('/')
def student():
    return render_template('student_template.html')

@app.route('/result',methods = ['POST', 'GET'])
def information():
    if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

    
if __name__ == '__main__':
   app.run(debug = True)
