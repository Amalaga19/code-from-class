from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    logged_in = True
    return render_template("loggedin.html", logged_in = logged_in)        

app.run(debug=True)
