from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/app")
def determiner():
    return render_template("determiner.html")

def receive_get():
    text = request.args["english_text"]
    if len(text) == 0:
        return "no text"
    else:
        return text

if __name__ == "__main__":
    app.run(debug=True)
