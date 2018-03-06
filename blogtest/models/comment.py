from blogtest.models import db
from blogtest.models.posts import Post

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.String(64), primaty_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DataTime())
    post_id = db.Column(db.String(64), db.ForeignKye("posts.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Comment {}>".format(self.name)
