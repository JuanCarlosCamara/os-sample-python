from flask import Flask
from gatos.ninja.backend.model import Model
application = Flask(__name__)


@application.route("/")
@application.route("/index")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    m = Model()
    m.create_default()

    application.run()
