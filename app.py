from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Assuming you have an index.html file in a templates folder "Flask is running successfully 🚀"

if __name__ == "__main__":
    app.run(debug=True)