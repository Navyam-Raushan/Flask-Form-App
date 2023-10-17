from flask import Flask, render_template

# Static folder is for images,, html, css and js
# Template folder is for html files

# Instance of web app
app = Flask(__name__)

# Rendering Home Page (/ represent home page
@app.route("/")
def index():
    return render_template("index.html")

app.run(debug=True, port=5001)