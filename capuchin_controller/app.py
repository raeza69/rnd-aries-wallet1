from flask import Flask, request, abort
from flask import jsonify
import sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'controller index page!'


@app.route('/webhooks/topic/connections/', methods=['POST'])
def webhooks():
    r = request.json
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    return 'success, 200'


@app.route('/webhooks/topic/basicmessages/', methods=['POST'])
def basicmessages():
    r = request.json
    print(r)
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    return 'success, 200'


@app.route('/webhooks/topic/issue_credential_v2_0/', methods=['POST'])
def credentials():
    r = request.json
    print(r)
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    return 'success, 200'
