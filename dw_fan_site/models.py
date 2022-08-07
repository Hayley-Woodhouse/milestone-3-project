from dw_fan_site import db


class Books(db.Model):
    # schema for the books model
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(25), unique=True, nullable=False)
    author_name = db.Column(db.String(25), unique=False, nullable=False)
    illustrator_name = db.Column(db.String(25), unique=False, nullable=False)
    publication_date = db.Column(db.Integer, nullable=False)
    synopsis_info = db.Column(db.Text, nullable=False)
    comment = db.relationship('Comment', backref='books', lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - {self.book_name} - Details:{self.author_name} - date:{self.publication_date}"


class Users(db.Model):
    # schema for the sign_up model
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(15), unique=False, nullable=False)
    l_name = db.Column(db.String(25), unique=False, nullable=False)
    email_user = db.Column(db.String(50), unique=True, nullable=False)
    password_user = db.Column(db.String(200), nullable=False)
    author = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - First Name:{self.f_name} - Last Name:{self.l_name}"


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    comment =db.Column(db.String(1000), unique=False, nullable=False)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    username = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Comment:{self.comment}"


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    images = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Comment:{self.images}"

