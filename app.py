from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#使用vscode 和git test
@app.route("/test")
def testgit():
    return "test"