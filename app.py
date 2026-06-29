from flask import Flask, render_template
app = Flask(__name__)  #contains main 
print(__name__)

@app.route("/")
def home():
    
    return render_template("home.html")

if (__name__ == "__main__"):
    app.run(host = "0.0.0.0", port = 5000, debug = False)  # host, port are optional, change in file server restart ->debug = true
    