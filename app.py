from flask import Flask
app =  Flask(__name__)
@app.route("/")
def home():
    return "hello this code was droped on Github"