from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server, Shell

from blogtest import create_app
from blogtest.models import db
from blogtest.models.user import Users
from blogtest.models.comment import Comment
from blogtest.models.posts import Post

app=create_app()
migrate=Migrate(app,db)
manager = Manager(app)

def make_context():
    return dict(**globals())

manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=make_context))
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()