from flask import Flask
application = Flask(__name__)


@application.route("/")
@application.route("/index")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    application.run()
