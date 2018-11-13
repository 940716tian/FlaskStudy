from flask_script import Manager

from myapp import create_app

app = create_app("debug")

manager = Manager(app)

if __name__ == "__main__":
    manager.run()