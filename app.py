from flask import Flask, render_template
from flask import request
from green

app = Flask(__name__)

@app.route("/", methods=["GET"])
def determiner():
    engText = request.args["english_text"]
    if len(engText) == 0:
        return render_template("determiner.html")
    else:
        result = green.article_identifier(engText)
        return render_template("determiner.html", result=result)

'''@app.route("/result", methods=["GET"])
def receive_get():
    text = request.args["english_text"]
    if len(text) == 0:
        return "no text"
    else:
        return text
'''
if __name__ == "__main__":
    app.run(debug=True)
