import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_message(username, message):
    """Add messages to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    # messages.append("({}) {}: {}".format(now, username, message))  Used before dict created below
    # messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append({"timestamp": now, "from": username, "message": message})

""" # This was removed when dict added above. Also, call from user() fn removed from return .format
def get_all_messages():
    # Get all messages and separate them with a 'br' tag
    return "<br>".join(messages)
"""


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with welcome & instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        # return redirect(session["username"])  Replaced by below. Also user() fn
        return redirect(url_for("user", username=session["username"]))

    # return "<h1>Hello World!</h1><p>To send a message: /USERNAME/MESSAGE</p>" Before render_template was added
    return render_template("index.html")


@app.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    """Add and Display Chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        # return redirect(session["username"])  Replaced by below. Also index() fn
        return redirect(url_for("user", username=session["username"]))

    # return "<h1>Welcome, {0}</h1> {1}".format(username, messages) otrequired once chat.html introduced
    return render_template("chat.html", username = username, chat_messages = messages)


""" Not required because messages are added via textbox
@app.route('/<username>/<message>')
def send_message(username, message):
    #Create a new message and redirect back to the chat page
    #return "{0}: {1}".format(username, message)
    add_message(username, message)
    return redirect("/" + username)  #returns the user to their personalised page
"""


app.run(
    host=os.environ.get("IP", "0.0.0.0"),
    port=int(os.environ.get("PORT", "5000")),
    debug=True
    )