from flask import Flask
from flask import render_template
from flask import request
from routes import register_blueprints

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World! This is from Flask! Here is more</p>"

@app.route("/about")
def about_page(name=None):
    return render_template('about.html', name="Abhinav")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return "This is a post request"
    else:
        return "This is a GET request"

register_blueprints(app)