from flask import Flask, request,render_template,redirect


app = Flask(__name__)

@app.route("/")
def index():
    return "tiams PhoneNumber: haooou AND kamys PhoneNumber is : 09175118377 AND rojas PhoneNumber is: 652"