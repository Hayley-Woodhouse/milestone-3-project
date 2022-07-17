from dw_fan_site import db


class Books(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(25), unique=True, nullable=False)
    detail = db.relationship("Details", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.book_name


class Details(db.Model):
    # schema for the details model
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(25), unique=True, nullable=False)
    illustrator_name = db.Column(db.String(25), unique=True, nullable=False)
    publication_date = db.Column(db.Integer, nullable=False)
    synopsis_info = db.Column(db.Text, nullable=False)
    books_id = db.Column(db.Integer, db.ForeignKey("books.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Details:{self.author_name} - date:{self.publication_date}"




