from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Slippy, Peppy, and Solt."

if __name__ == "__main__":
    app.run()