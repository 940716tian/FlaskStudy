from flask_script import Manager
from myapp import create_app
from flask_migrate import MigrateCommand

app = create_app("debug")
app.app_context().push()
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()