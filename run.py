import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """Get all messages and separate them with a 'br' tag"""
    return "<br>".join(messages)


@app.route('/')
def index():
    """Main page with welcome & instructions"""
    return "<h1>Hello World!</h1><p>To send a message: /USERNAME/MESSAGE</p>"


@app.route('/<username>')
def user(username):
    """Display Chat messages"""
    return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    #return "{0}: {1}".format(username, message)
    add_messages(username, message)
    return redirect("/" + username)  #returns the user to their personalised page


app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True
    )