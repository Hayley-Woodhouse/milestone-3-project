from flask import flash, render_template, request, session, redirect, url_for
from dw_fan_site import app, db
from dw_fan_site.models import Books, Users, Comment
from werkzeug.security import generate_password_hash, check_password_hash



# # route to render the home page
@app.route("/")
def home():
    return render_template("home.html")


# route to render the books/library page
@app.route("/books", methods=["GET", "POST"])
def books():
    comment = list(Comment.query.order_by(Comment.id).all())
    books = list(Books.query.order_by(Books.book_name).all())
    return render_template("books.html", books=books, comment=comment) 


# route to render the add_book page
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    books = list(Books.query.order_by(Books.book_name).all())
    if request.method == "POST":
        # from form on add_book page these fields are filled in
        book = Books(
            book_name=request.form.get("book_name"),
            author_name=request.form.get("author_name"),
            illustrator_name=request.form.get("illustrator_name"),
            publication_date=request.form.get("publication_date"),
            synopsis_info=request.form.get("synopsis_info"),
            id=request.form.get("book_id")
        )
        # pushed to the db
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("books"))
    return render_template("add_book.html", books=books)


# route to render the edit_book page
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


# route to delete book from db
@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    booked = Books.query.get_or_404(book_id)
    db.session.delete(booked)
    db.session.commit()
    return redirect(url_for("books"))

# route to render the edit_user page
@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = Users.query.get_or_404(user_id)
    if request.method == "POST":
        user.id = user_id
        user.f_name = request.form.get("f_name"),
        user.l_name = request.form.get("l_name"),
        user.email_user = request.form.get("email_user"),
        db.session.commit()
        return redirect(url_for("admin"))
    return render_template("edit_user.html", user=user)

# route to delete Users from db
@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    Used = User.query.get_or_404(user_id)
    db.session.delete(booked)
    db.session.commit()
    return redirect(url_for("admin"))


# route to render the sign_page
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
            # pushed to the db
            db.session.add(users)
            db.session.commit()
            flash("Sign-up was Successful!")
            return redirect("login")
    return render_template("sign_up.html")


# route to render the login page
@app.route("/login", methods=["GET", "POST"])  
def login():
    if request.method == "POST":
        email_user=request.form.get("email_user")
        password1=request.form.get("password_user")
        personObject = Users.query.filter_by(email_user=email_user).first()
        if personObject:
            # make sure hashed password matches users input 
            if check_password_hash(personObject.password_user, password1):
                if "admin" == email_user:
                    session["admin"] = email_user
                    return redirect(url_for("admin"))
                else:
                    session["name"] = email_user
                    return redirect(url_for("profile", usernameIn=personObject.f_name))
            else:
                # invalid password
                flash("Incorrect Username and/or Password")
        else:
            # invalid User(email)
            flash("Incorrect Username and/or Password")
    return render_template("login.html")


# route to render the profile page
@app.route("/profile/<usernameIn>", methods=["GET", "POST"])
def profile(usernameIn):

    if session.get("name"):
        return render_template("profile.html", usernameIn=usernameIn)
    return redirect(url_for("login"))


# route to render the admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    users = list(Users.query.order_by(Users.f_name).all())
    if session["admin"]:
        return render_template("admin.html", users=users)
    return redirect(url_for("login"))


# route to logout of profile page
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    if session.get("name"):
        session.pop("name")
    else:
        session.pop("admin")
    return redirect(url_for("login"))


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    bookget = Books.query.first()
    if request.method == "POST":
       
        comment = Comment(
            comment=request.form.get("comment"),
            id=request.form.get("comment_id"),
            books_id=bookget.id
        )
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('books'))


    






