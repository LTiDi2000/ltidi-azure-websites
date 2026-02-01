from flask import Flask
app = Flask(__name__)

@app.route("/thaivu")
def hellothaivu():
    return "Hello, thaivu PoC!"

@app.route("/ltidi")
def helloltidi():
    return "Hello, ltidi PoC!"

@app.route("/pt200")
def hellopt200():
    return "Hello, pt200 PoC!"

@app.route("/flysec")
def helloflysec():
    return "Hello, flysec PoC!"

@app.route("/")
def hello():
    return "Hello, whitehat PoC!"
