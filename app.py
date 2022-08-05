from flask import *
from flask_socketio import SocketIO
import green

app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)

result = []

@app.route("/")
def determiner():
    return render_template("determiner.html", result=result)

@app.route("/result", methods=["GET", "POST"])
def get_form():
    global engStr

    try:
        engStr = request.form["english_text"]
    except:
        engStr = ""

    result = green.run(engStr)

    sub = 0
    print(result)

    if len(result) == 0:
        return render_template("determiner.html", result=['error'], engStr="ERROR: The English sentence is wrong.")

    while '_' in engStr:

        index = engStr.find('_')
        engStr = engStr[:index] + str(result[sub][1]) + engStr[index+1:]
        sub += 1

    return render_template("determiner.html", result=result, engStr=engStr)

if __name__ == "__main__":
    app.run(debug=True)
