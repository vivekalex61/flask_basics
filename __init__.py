import os

from flask import Flask


from flask import Flask, redirect, url_for, request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    #this sets path of the web application address and the path run corresponding function 
    @app.route('/<int:postid>')#here thr path is some imtegern id.if we write some number ir will get the number and print tje number 
    def hello(postid):#function that runs ehrn the path is valled 
        return 'Hello, World!'+str(postid)
    
    @app.route('/admin')#path 
    def hello_admin():#function that runs ehrn the path is valied 
        return 'Hello, admin'

    @app.route('/guest')#path 
    def hello_guest():#function that runs ehrn the path is valied 
        return 'Hello, guest'
    
    @app.route('/login_success/<name>')#path 
    def hello_login(name):#function that runs ehrn the path is valled 
        return 'welcome '+str(name)

    '''
    url_for() function calls a route or url already build '''

    @app.route('/<name>')#path 
    def hello_name(name):#function that runs ehrn the path is valled 
        if name=='admin':
            return redirect(url_for(hello_admin))#redircting tje url to admin
        else:
            return redirect(url_for(hello_guest))#redircting the url to guest


#HTML PAGE Manipulation
#created html login page


    
    @app.route('/login',methods=['POST'])#path 
    def login():#function that runs ehrn the path is valled 
           if request.method == 'POST':
                user = request.form['nm']
                return redirect(url_for('hello_login',name = user))

    return app
