from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def determiner():
    return render_template("determiner.html")

@app.route("/result", methods=["GET"])
def receive_get():
    text = request.args["english_text"]
    if len(text) == 0:
        return "no text"
    else:
        return text

if __name__ == "__main__":
    app.run(debug=True)
