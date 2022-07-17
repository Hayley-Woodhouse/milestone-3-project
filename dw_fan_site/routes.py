from flask import render_template
from dw_fan_site import app, db

@app.route("/")
def home():
    return render_template("base.html")