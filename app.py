from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "ssatosays": "password",
    "ssatosays1": "password",
    "ssatosays2": "password",
    "ssatosays3": "password"
}


@auth.get_password
def get_password(username):
    if username in users:
        return users.get(username)
    return None


@app.route("/")
@auth.login_required
def index():
    return "Hello, {}!".format(auth.username())


if __name__ == "__main__":
    app.run(debug=True)
