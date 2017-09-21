from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import db
from wsgi import app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
