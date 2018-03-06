from blogtest.models import db
from blogtest.models.user import Users
from blogtest.models.comment import Comment

posts_tags=db.Table(
    "posts_tags",
    db.Column("post_id",db.String(64),db.foreignKey("posts.id")),
    db.Column("tag_id",db.String(64),db.ForeignKey("tags.id")),
)

class Post(db.Model):
    __tablename__="posts"

    id=db.Column(db.String(64),primary_key=True)
    title=db.Column(db.String(255))
    text=db.Column(db.Text)
    publish_date=db.Column(db.Datetime)

    user_id=db.Column(db.String(64),db.ForeignKey("users.id"))

    comments=db.relationship(
        "Comment",
        backref="posts",
        lazy="dynamic",
    )

    tags=db.relationship(
        "Tag",
        backref="posts",
        lazy="dynamic",
        secondary=posts_tags,
    )

    def __init__(self, title):
        self.title=title

    def __repr__(self):
        return "<Module Post {}>".format(self.title)


class Tag(db.Model):
    id=db.Column(db.String(64),primary_key=True)
    name=db.Column(db.Striing(255))

    def __int__(self,name):
        self.name=name

    def __repr__(self):
        return "<Model Tag {}>".format(self.name)