from flask import render_template
from dw_fan_site import app, db
from dw_fan_site.models import Books, Details


@app.route("/")
def home():
    return render_template("newbook.html")