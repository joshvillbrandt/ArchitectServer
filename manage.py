from flask.ext.script import Server, Manager
from Architect import app

# make manager
manager = Manager(app)
manager.add_command("runserver", Server(
	use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0'))

if __name__ == "__main__":
    manager.run()