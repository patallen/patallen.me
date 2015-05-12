from flask import render_template
from app import app

@app.route('/')
def home():
	"""Static home page"""
    return render_template('base.html')

@app.route("/contact/")
def contact():
	"""Static contact page"""
    return "Contact me"
