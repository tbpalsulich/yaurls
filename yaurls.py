# Tyler Palsulich

import json
import random
import string

from flask import Flask, request, redirect, url_for, abort, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# Create our database model
class Redirect(db.Model):
    __tablename__ = "redirects"
    slug = db.Column(db.String(6), primary_key=True)
    url = db.Column(db.String(2083))

    def __init__(self, slug, url):
        self.slug = slug
        self.url = url

# http://stackoverflow.com/a/2257449
def random_string(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    slug = random_string(6)
    redir = Redirect(slug, request.form['url'])
    db.session.add(redir)
    db.session.commit()
    return json.dumps({"slug": slug})

@app.route("/<slug>")
def get(slug):
    redir = db.session.query(Redirect).get(slug)
    if redir is None: abort(404)

    return redirect(redir.url)

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
