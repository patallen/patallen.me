from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('base.html')

@app.route("/contact/")
def contact():
    return "Contact me"
