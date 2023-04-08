from flask import Flask,render_template

application = Flask(__name__)

@application.route("/")
def home():
    return "Home page working"

@application.route("/indexpage")
def index():
    return render_template("index.html")

if __name__=="__main__":
    application.run(host="0.0.0.0")