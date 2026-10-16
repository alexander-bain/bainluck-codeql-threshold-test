"""Static-only synthetic fixture. This application is never started or deployed."""
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/controlled-fixture")
def controlled_fixture():
    response = make_response("Synthetic test only")
    response.set_cookie(
        "sessionid", value="synthetic-test-only", secure=True, httponly=True, samesite="Strict"
    )
    return response
