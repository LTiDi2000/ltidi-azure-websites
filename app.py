from flask import Flask
app = Flask(__name__)

@app.route("/thaivu")
def hello():
    return "Hello, whitehat PoC!"
