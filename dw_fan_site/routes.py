from flask import flash, render_template, request, redirect, url_for
from dw_fan_site import app, db
from dw_fan_site.models import Books, Users
from werkzeug.security import generate_password_hash, check_password_hash


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
            id=request.form.get("book_id")
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books"))
    return render_template("add_book.html", books=books)


@app.route("/sign_up", methods=["GET", "POST"])  
def sign_up():
    if request.method == "POST":
        email_user=request.form.get("email_user")
        password1=request.form.get("password_user")
        password2=request.form.get("password2")
    
        # check if username already exists in db
        email = Users.query.filter_by(email_user=email_user).first()
        if email:
            flash("email already used!")
            return redirect(url_for("sign_up"))

        # check if passwords match
        elif password1 != password2:
            flash("passwords do no match!")
            return redirect(url_for("sign_up"))
        else:
            users = Users(
                f_name=request.form.get("f_name"),
                l_name=request.form.get("l_name"),
                email_user=email_user,
                password_user=generate_password_hash(password1, method='sha256'),
                id=request.form.get("users_id")
                )
            db.session.add(users)
            db.session.commit()
            flash("Sign-up was Successful!")
            return redirect("login")
    return render_template("sign_up.html")



    # if existing_user:
    #     flash("This user already exists")
    #     return redirect(url_for("sign_up"))

    # return render_template("sign_up.html") 


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
        # check if username already exists in db
        # existing_user = mongo.db.users.find_one(
        #     {"username": request.form.get("username").lower()})

        # if existing_user:
        #     flash("Username already exists")
        #     return redirect(url_for("register"))

        # register = {
        #     "username": request.form.get("username").lower(),
        #     "password": generate_password_hash(request.form.get("password"))
        # }
        # mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
    #     session["user"] = request.form.get("username").lower()
    #     flash("Registration Successful!")
    # return render_template("register.html")

@app.route("/login")  
def login():
    return render_template("login.html")


@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = Books.query.get_or_404(book_id)
    if request.method == "POST":
        book.id = book_id
        book.book_name = request.form.get("book_name"),
        book.author_name = request.form.get("author_name"),
        book.illustrator_name = request.form.get("illustrator_name"),
        book.publication_date = request.form.get("publication_date"),
        book.synopsis_info = request.form.get("synopsis_info"),
        db.session.commit()
        return redirect(url_for("books"))
    return render_template("edit_book.html", book=book)


@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    booked = Books.query.get_or_404(book_id)
    db.session.delete(booked)
    db.session.commit()
    return redirect(url_for("books"))