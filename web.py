from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/index.html")
def cohort_three():
    return ("Welcome to cohort three")

@app.route("/home")
def profile():
    return ("My name is Sherry")

@app.route("/templates")
def templatesm():
    return render_template("index.html")
app.run()