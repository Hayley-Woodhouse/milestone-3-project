from flask import render_template, request, redirect, url_for
from dw_fan_site import app, db
from dw_fan_site.models import Books


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/books")  
def books():
    return render_template("books.html") 


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        books = Books(book_name=request.form.get("book_name"))
        db.session.add(books)
        db.session.commit()
        return redirect(url_for("books"))
    return render_template("add_book.html") 
