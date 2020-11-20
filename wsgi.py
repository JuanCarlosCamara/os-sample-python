from flask import Flask
from gatos.ninja.backend.model import Model
application = Flask(__name__)
m = Model()

@application.route("/")
@application.route("/index")
def hello():
    return "Hello World!"


@application.route("/getuser/<user_id>")
def get_user_info(user_id):
    user_info = m.get_user_info(user_id)
    return user_info.to_json()


if __name__ == "__main__":
    m.create_default()

    application.run()
