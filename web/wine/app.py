import os
import random
import string
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

COMPLAINTS_DIR = 'complaints'
os.makedirs(COMPLAINTS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complaint', methods=['GET'])
def complaint():
    i = request.args.get('id')
    if i is None:
        return render_template('error.html', message="no complaint specified"), 400

    path = make_path(i)
    print(path)
    try:
        with open(path) as f:
            complaint = f.read()
    except FileNotFoundError:
        return render_template('error.html', message=f"{path} not found"), 404

    return render_template('complaint.html', content=complaint)

@app.route('/complaint', methods=['POST'])
def make_complaint():
    i = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    content = request.form.get('content')

    path = make_path(i)
    with open(path, 'w') as f:
        f.write(content)

    return redirect(url_for('complaint') + '?id=' + i)

def make_path(i):
    path = os.path.join(COMPLAINTS_DIR, i) + '.txt'
    path = path[:40]
    return path

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
