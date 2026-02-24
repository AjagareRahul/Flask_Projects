from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1>Hello Admin</h1>"

@app.route("/librarian")
def librarian():
    return "<h1>Hello Librarian</h1>"

@app.route("/student")
def student():
    return "<h1>Hello Student</h1>"

@app.route("/user/<username>")
def user(username):
    if username == "admin":
        return redirect(url_for("admin"))
    elif username == "librarian":
        return redirect(url_for("librarian"))
    elif username == "student":
        return redirect(url_for("student"))
    else:
        return "<h1>Hello User</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)