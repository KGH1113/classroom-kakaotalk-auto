from modules.getMessage import getMessage
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/getMessage", methods=["POST"])
def api_getMessage():
    # body = request.get_json()
    # print(body)
    # print(body["userRequest"]["utterance"])

    responseBody = {
        "version": "2.0",
        "template": {"outputs": [{"simpleText": {"text": getMessage()}}]},
    }

    return responseBody
