from flask import Flask, redirect, render_template, request
app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('uploadfile.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('success.html', fname=f.filename)
    else:
        return "Try Again"
    
if __name__ == '__main__':
    app.run(debug=True)
