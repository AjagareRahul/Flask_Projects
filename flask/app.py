from flask import Flask, render_template
app=Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def home():
    name="Rahul"
    return render_template("index.html", fname=name) 

@app.route("/homes/<name>")
def homes(name):
    
    return render_template("home.html", fname=name)

@app.route("/table/<int:num>")
def contact(num):
    for i in range(1,11):
        print(f"{i} * {num} = {i * num}")
    
    return render_template("index.html", num=num)

if __name__=="__main__":
    app.run()