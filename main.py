from flask import Flask

app = Flask(__name__)

@app.route("/")
def chat():
    return

@app.route("/resume")
def resume():
    return

@app.route("/interview")
def interview():
    return


app.run(debug=True)