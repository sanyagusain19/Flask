from flask import Flask, render_template, request
import os

app = Flask(__name__)  # contains main
print(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # In this simple app we don't store messages; just acknowledge receipt
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        return render_template("contact.html", sent=True, name=name)
    return render_template("contact.html", sent=False)

if __name__ == "__main__":
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host=host, port=port, debug=debug)
