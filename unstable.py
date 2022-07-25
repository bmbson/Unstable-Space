import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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

    @app.route("/admin")
    def admin():
        return render_template("admin.html")
    

    return app