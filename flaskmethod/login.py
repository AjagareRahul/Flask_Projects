from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def register():
    return render_template('registration.html')

@app.route('/success', methods=['POST', 'GET'])
def success():
    if request.method == 'POST':
        result = request.form
        return render_template("show.html", result=result)
    else:
        return render_template("registration.html")
     
'''      
@app.route('/login', methods=['GET'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'Rahul' and password == 'Rahul2004':
        return "Login successful: %s" % username
    else:
        return "Login failed"
    

@app.route('/login')
def loginform():
    return render_template('form.html')
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'Rahul' and password == 'Rahul2004':
        return "Login successful: %s" % username
    else:
        return "Login failed" ''' 

if __name__ == '__main__':
    app.run(debug=True)