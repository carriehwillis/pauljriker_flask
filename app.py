from flask import Flask, render_template
from helper import menu_items

app = Flask(__name__, template_folder="templates")

@app.route("/")
@app.route("/index.html")
@app.route("/home.html")
def index():
    return render_template("index.html", menu_items = menu_items)

@app.route("/works.html")
def works():
    return render_template("works.html", menu_items = menu_items)

@app.route("/contact.html")
def contact():
    return render_template("contact.html", menu_items = menu_items)


if __name__ == "__main__":
    app.run(debug=True)