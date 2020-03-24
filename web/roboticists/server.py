import flask
from flask import Flask
from flask import request, send_file, url_for

import codecs
import base64

app = Flask(__name__)

@app.route('/robots.txt', methods=['GET'])
def robots():
	return send_file('robots.txt', attachment_filename='robots.txt')
	

@app.route("/", methods=['GET', 'POST'])
def root():

    resp = flask.make_response(flask.render_template('message.html'))
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
