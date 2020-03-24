import sqlite3
import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.redirect('index.html')


@app.route('/<path:filename>')
def static_files(filename):
    return flask.send_from_directory('files', filename)


@app.route('/api/flag/<string:flag>')
def get_flag(flag):
    conn = sqlite3.connect('flags.db')
    cur = conn.cursor()

    try:
        query = "SELECT flag FROM fakeflags WHERE name='" + flag + "'"
        print(query)
        cur.execute(query)
        res = cur.fetchone()[0]
        if res is None:
            return ''
        else:
            return res
    except (TypeError, ValueError):
        return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
