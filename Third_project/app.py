from flask import Flask, request
app=Flask(__name__)

# Debug: Log when app starts
print("=" * 50)
print("Third_project Flask app starting on port 5000")
print("=" * 50)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about/<name>")
def about_name(name="Guest"):
    return f"<p>About {name}</p>"

@app.route("/contact")
def contact():
    return "<p>Contact</p>"

@app.route("/home")
def home():
    return "<p>Home</p>"
if __name__=="__main__":
    app.run(debug=True,port=5001)
    