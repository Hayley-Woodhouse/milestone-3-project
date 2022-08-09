from dw_fan_site import db


class Books(db.Model):
    # schema for the books model
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(25), unique=True, nullable=False)
    author_name = db.Column(db.String(25), unique=False, nullable=False)
    illustrator_name = db.Column(db.String(25), unique=False, nullable=False)
    publication_date = db.Column(db.Integer, nullable=False)
    synopsis_info = db.Column(db.Text, nullable=False)
    # comments can have many posts
    comment = db.relationship('Comment', backref='books', cascade='all, delete')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - {self.book_name} - Details:{self.author_name} - date:{self.publication_date}"


class Users(db.Model):
    # schema for the sign_up model
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(15), unique=False, nullable=False)
    l_name = db.Column(db.String(25), unique=False, nullable=False)
    email_user = db.Column(db.String(50), unique=True, nullable=False)
    password_user = db.Column(db.String(200), nullable=False)
    # comments can have many posts
    users = db.relationship('Comment', backref='users', cascade='all, delete')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - First Name:{self.f_name} - Last Name:{self.l_name}"


class Comment(db.Model):
    # schema for the comment model
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(1000), unique=False, nullable=False)
    # Foreign key to link books (refer to primary key to the book)
    books_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    # Foreign key to link users (refer to primary key to the users)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Comment:{self.comment}"