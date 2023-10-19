from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Static folder is for images,, html, css and js
# Template folder is for html files

# Instance of web app
app = Flask(__name__)

# These are some secret keys and database instance.
app.config["SECRET_KEY"] = "myapplication"

# This will be the file name of database = data.db (avoid typos)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# Instance of database
db = SQLAlchemy(app)


# Database Columns name (db.Capital_letter)
# Making Columns in database it will take datatypes
# column_name = db.Column(db.Data_type)
# Here table name will be = class name
class Form(db.Model):
    # A Table to store the data.
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


# Rendering Home Page (/ represent home page
# We have to give GET AND POST methods.
# request.form is a dictionary which have all html element values.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        start_date = request.form["date"]
        occupation = request.form["occupation"]

        print(first_name, last_name, email, start_date, occupation)

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        # The db will create the table that is in db.Model
        db.create_all()
        app.run(debug=True, port=5001)
