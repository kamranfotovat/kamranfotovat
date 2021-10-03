from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "post":
        pass

    if request.method == "get":
        return render_template("login.html")