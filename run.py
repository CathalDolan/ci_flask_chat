import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with welcome & instructions"""
    return "<h1>Hello World!</h1><p>To send a message: /USERNAME/MESSAGE</p>"


@app.route('/<username>')
def user(username):
    # Creates the Username
    return "Hi " + username


@app.route('/<username>/<message>')
def send_message(username, message):
    # Creates the message
    return "{0}: {1}".format(username, message)
    return "Message " + message


app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True
    )