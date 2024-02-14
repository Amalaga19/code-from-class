from flask import Flask, render_template

app = Flask(__name__)

beatles = [
    "John", "George", "Ringo", "Paul",
]

@app.route("/")
def index():
    return render_template("beatles.html", names = beatles)


app.run(debug=True)
