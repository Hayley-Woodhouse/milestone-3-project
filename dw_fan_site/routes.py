from flask import render_template, request, redirect, url_for
from dw_fan_site import app, db
from dw_fan_site.models import Books


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/books")  
def books():
    books = list(Books.query.order_by(Books.book_name).all())
    return render_template("books.html", books=books) 


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    books = list(Books.query.order_by(Books.book_name).all())
    if request.method == "POST":
        book = Books(
            book_name=request.form.get("book_name"),
            author_name=request.form.get("author_name"),
            illustrator_name=request.form.get("illustrator_name"),
            publication_date=request.form.get("publication_date"),
            synopsis_info=request.form.get("synopsis_info"),
            # books_id=request.form.get("books_id")
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books"))
    return render_template("add_book.html", books=books)