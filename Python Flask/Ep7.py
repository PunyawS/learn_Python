from flask import Flask #import library

app = Flask(__name__) #Name mudule

@app.route('/')
def index():
    return "<h1>Hello Flask Framwork</h1>" #Show Text

@app.route('/about') #http://127.0.0.1:5000/about
def about():
    return '<h1>about me</h1>'

@app.route('/admin') #http://127.0.0.1:5000/admin
def profile():
    return '<h1>Hello admin</h1>'

if __name__ == "__main__":
    app.run() #Run Web server