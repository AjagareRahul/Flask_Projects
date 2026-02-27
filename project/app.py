from flask import Flask, redirect, request, render_template, make_response
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username == 'Rahul' and email == 'ajagarerahul@gmail.com' and password == 'Rahul2004':
            resp = make_response(redirect('/success'))
            resp.set_cookie('username', username)
            resp.set_cookie('email', email)
            return resp
        else:
            return redirect('/error')
        
    return render_template('login.html')


@app.route('/success')
def success():
    return render_template('success.html')

   


@app.route('/profile')
def profile():
  
    us = request.cookies.get('username')
    em = request.cookies.get('email')
    return render_template('profile.html', fname=us, femail=em) 


@app.route('/error')
def error():
    return render_template('error.html', error_message="Invalid username, email, or password. Please try again.")


if __name__ == '__main__':
    app.run(debug=True)
