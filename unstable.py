from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def front():
    return render_template("front.html")

@app.route("/mixes")
def mixes():
    return render_template("mixes.html")

@app.route("/block")
def blog():
    return render_template()
    
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/merch")
def merch():
    return render_template()
    
@app.route("/contact")
def contact():
    return render_template("contact.html")
 
@app.route("/secret")
def secret():
    return render_template("secret.html")