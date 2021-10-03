from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST","GET"])
def login():

    if request.method == "post":

        name = request.form.get("username")
        password = request.g=form.get("password")


        if not name:
            pass

        if not password:
            pass


    if request.method == "get":
        return render_template("login.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "post":

        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not name:
            pass

        if not password:
            pass

        if not confirmation:
            pass

        if password != confirmation:
            pass





    if request.method == "get":
        return render_template("register.html")