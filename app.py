from flask import Flask
app = Flask(__name__) #flask类的实例化

@app.route("/")
def hello_world():
    return "<p>Please select the file u want to upload:</p>"

