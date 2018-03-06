from blogtest.models import db


class Users(db.Model):
    __tablename__="users"

    id=db.Column(db.String(64),primary_key=True)
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))

    posts=db.relationship(
        "Post",
        backref="users",
        lazy="dynamic",
    )

    def __init__(self, id, username,password):
        self.id=id
        self.username=username
        self.password=password

    def __repr__(self):
        return "<Model User  {}>".format(self.username)
