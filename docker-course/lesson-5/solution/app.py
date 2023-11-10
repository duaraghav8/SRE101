from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def hello():
    return "PONG"


# The default port used by Flask to bind to is 5000.
# So we need not explicitly specify unless we want to bind to some other port.
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
