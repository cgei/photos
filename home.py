from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("working")
    return "<button>Hedge</button>"

@app.route("/about")
def about():
    return "blessed"
