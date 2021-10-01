from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from unknown import apology, login_required

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")