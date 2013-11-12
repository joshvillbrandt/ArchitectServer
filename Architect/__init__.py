from flask import Flask
from flask.ext.mongoengine import MongoEngine


# make app
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "architect_test"}
app.config["SECRET_KEY"] = "KeeafdsfdasdsfapThisdfadfdfadfsaS3cr3t"

db = MongoEngine(app)

@app.route('/')
def index():
    return render_template('index.html', STATIC_URL='/static/')

if __name__ == '__main__':
    app.run()