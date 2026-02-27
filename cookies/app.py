from flask import Flask, render_template, request, make_response 
app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    resp = make_response(render_template('cookies.html'))
    resp.set_cookie('username', 'John Doe')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return render_template('cookies.html', username=username)
    else:
        return "No cookie found! Visit /setcookie first."

if __name__ == '__main__':
    app.run(debug=True)