from flask import Flask #import library

app = Flask(__name__) #Name mudule

@app.route('/hello') #URL http://127.0.0.1:5000/hello
def index():
    return "<h1>Hello Flask Framwork</h1>" #Show Text

if __name__ == "__main__":
    app.run() #Run Web server