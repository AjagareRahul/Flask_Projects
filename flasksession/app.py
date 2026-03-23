from flask import Flask, make_response , render_template , request , redirect , url_for , session , flash
from flask_session import Session
app = Flask(__name__)
app.secret_key = 'abc'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)



@app.route('/')
def sessions():
    resp = make_response("<h1>Welcome to the Flask Session Example</h1> <a href='/getsession'>Get Session Data</a>")
    
    session['username'] = 'Rahul'
    session['email'] = 'rahul@gmail.com'
    return resp

@app.route('/getsession')
def getsession():
    return f"Username: {session['username']}, Email: {session['email']}"


if __name__ == '__main__':
    app.run(debug=True)
    
    