from flask import Flask, request, abort, render_template
from flask import jsonify
import sys

jsn = []
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'controller index page genting!'


@app.route('/webhooks/topic/connections/', methods=['POST'])
def webhooks():
    r = request.json
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    return 'success, 200'


@app.route('/webhooks/topic/basicmessages/', methods=['POST','GET'])
def basicmessages():
    r = request.json
    print(r)
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    jsn.append(r)
    return render_template('index.html',output=jsn)


@app.route('/webhooks/topic/issue_credential_v2_0/', methods=['POST'])
def credentials():
    r = request.json
    print(r)
    print("Response : ", r, file=sys.stderr)  # output response logs.
    print("stdout", r, file=sys.stdout)  # supposed to output here
    return 'success, 200'
