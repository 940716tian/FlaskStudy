from myapp.extensions import db

class Dog(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )
    place = db.Column(
        db.String(50),
        default="杭州户口"
    )

    def to_dict(self):
        data = {
            "id":self.id,
            "name":self.name,
            "place":self.place
        }
        return data

class Grade(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        unique=True
    )
    stus = db.relationship(
        "Stu",
        backref="grade",
        lazy=True
    )

class Stu(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
        unique=True
    )
    grade_id = db.Column(
        db.Integer,
        db.ForeignKey("grade.id")
    )

class Tag(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    title = db.Column(
        db.String(20)
    )

tags = db.Table(
    "tags",
    db.Column("tag_id",db.Integer,db.ForeignKey("tag.id"),primary_key=True ),
    db.Column("book_id",db.Integer,db.ForeignKey("book.id"),primary_key=True ),
)

class Book(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(20),
    )
    tags = db.relationship(
        "Tag",
        secondary=tags,
        backref=db.backref("books",lazy=True),
        lazy=True

    )