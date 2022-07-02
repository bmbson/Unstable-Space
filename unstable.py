from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def front():
    return render_template("front.html")

def mixes():
    return render_template()

def blog():
    return render_template()

def gallery():
    return render_template()

def about():
    return render_template()

def merch():
    return render_template()

def contact():
    return render_template()
 
