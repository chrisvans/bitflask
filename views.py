from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Slippy, Peppy, and Solt."


@app.route("/add")
def add():
    from models import Link
    newlink = Link(name='newlink', link='www.google.com')
    db.session.add(newlink)
    db.session.commit()
    result = str(newlink)
    return result


@app.route("/view")
def view():
    from models import Link
    result = str(Link.query.all())
    return result


@app.route("/create-table-link")
def create_table_link():
    return 


if __name__ == "__main__":
    app.run()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()