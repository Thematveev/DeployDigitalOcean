from flask import Flask
from data import CARS, USERS

app = Flask(__name__)


@app.route('/cars')
def cars():
    return CARS

@app.route('/users')
def users():
    return USERS


if __name__ == "__main__":
    app.run()