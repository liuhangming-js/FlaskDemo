from flask import Flask, escape, url_for, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/author')
def author():
    return 'Johnson Liu'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is {}'.format(escape(username))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return index()
    else:
        return 'You should use Post method.'


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./files/' + secure_filename(f.filename))
        return jsonify(message='File uploaded successfully')
    else:
        return jsonify(message='File uploaded filed')


with app.test_request_context():
    print(url_for('index'))
    print(url_for('author', next='/'))
    print(url_for('show_user_profile', username='Johnson'))
