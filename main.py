from flask import Flask, request, redirect,render_template
#import cgi
#import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    # render the template using the shortcut from flask called render_template
    return render_template('user-signup.html')

@app.route('/', methods=['POST','GET'])
def validate_form():

    username = request.form['username'] 
    password = request.form['password'] 
    verify = request.form['verify']
    email = request.form['email']

    username_error = '' 
    password_error = '' 
    verify_error = ''
    email_error = ''  

    #test validity of the username
    if len(username) < 3 or len(username) > 20:
        username_error = 'Not a valid username'
     

    if ' ' in username:
        username_error = 'Not a valid username'        

    #test the validity of the password
    if len(password) < 3 or len(password) > 20:
        password_error = 'Not a valid password'
        password = ''

    if ' ' in password:
        password_error = 'Not a valid password'
        password = ''

    #test the validity of the verify password box
    if verify != password or len(verify) == 0:
        verify_error = 'Not a valid password verification'
        verify = ''

    #if any text in email field, test it
    #a single @, a single ., contains no spaces
    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            email_error = 'Not a valid email'
        if '.' not in email:
            email_error = 'Not a valid email'
        if '@' not in email:
            email_error = 'Not a valid email'
        if ' ' in email:
            email_error = 'Not a valid email'
                        

    # if form is valid render welcome page
    if len(username_error) > 0 or len(password_error) > 0 or len(verify_error) > 0 or len(email_error) > 0:
        return render_template('user-signup.html',password_error=password_error, username_error=username_error,
        verify_error=verify_error,email_error=email_error)        
    else:
        return render_template('welcome.html',username=username)


app.run()