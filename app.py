print("App is starting...")
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    year = request.form["year"]
    return render_template("success.html", name=name, year=year)

app.run(debug=True)