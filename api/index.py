# Import of all the library used in this project
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import random
import string
from flask_mail import Mail, Message

# Configure app
app = Flask(__name__)

# Configuration Of Auto Reload Of All The Templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template('api_test_add.html')


@app.route("/add", methods=['POST'])
def add():
    if request.method == 'POST':
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        email = request.form.get("email")
        password = request.form.get("password")
        params = {"f_name": f_name, "l_name": l_name,
                  "email": email, "password": password}
        post_url = requests.post(
            'http://coderashapi.mywebcommunity.org/data_add.php', data=params)
        response = post_url.json()
        messages = response["message"]
    return render_template('api_test_add.html', response=messages)


@app.route("/fetch")
def fetch():
    post_url = requests.get(
        'http://coderashapi.mywebcommunity.org/data_fetch.php')
    response = post_url.json()
    message = response["message"]
    records = {"data": response['data'][::2]}

    return render_template('api_test_fetch.html', data=records, response=message)
