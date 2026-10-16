"""Official CodeQL cookie regression specimen; analyzed statically, never run."""
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/test")
def test():
    resp = make_response()
    resp.set_cookie("authKey", "value1")
    return resp
