from flask import Flask,render_template
app=Flask(__name__)
@app.route('/<user>')
def html_output(user):
    #return '<html><body><h1>Here the html </h1></body></html>'
    #or 
    return render_template('simpl.html',name=user)
 


#it is is very cooplex to retunr the html function because of length of code . so we can  pass a html file instead of the html code
#we use render_template() function .we can pass the .html file  inside the function
if __name__ == '__main__':
   app.run(debug = True)