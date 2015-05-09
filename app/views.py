from app import app

@app.route('/')
def home():
    return "This is the home page"

@app.route("/work/")
def portfolio():
    return "This is the portoflio page"

@app.route("/contact/")
def contact():
    return "Contact me"
