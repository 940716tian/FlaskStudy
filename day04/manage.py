from flask import Flask
from flask_script import Manager
from myapp import create_app
from flask_migrate import MigrateCommand

app = create_app("debug")
manager = Manager(app)
manager.add_command("db",MigrateCommand)
app = Flask(__name__)

if __name__ == '__main__':
    manager.run()
