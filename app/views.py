from app import app

@app.route('/')
def home():
    return "This is the home page"

@app.route("/blog/")
def blog():
    return "This is the main blog page"

@app.route("/blog/<int:post_id>/")
def blogpost(post_id):
    return "This is blog post {}".format(post_id)

@app.route("/work/")
def portfolio():
    return "This is the portoflio page"

@app.route("/contact/")
def contact():
    return "Contact me"
