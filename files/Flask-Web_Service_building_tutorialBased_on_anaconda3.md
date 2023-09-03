# Flask-Web Service building tutorial(Based on anaconda3)

## 1 Python environment

I'm not going to repeat how to install anaconda, assuming that work has already been done.

First we should stablish virtual environment in anaconda（I'm used to use python 3.8，which is compatible for many elder repository）。

```powershell
conda create -n flask python=3.8
conda activate flask
```

Then install the dependence

```powershell
pip install Flask
```

## 2 Fresh start

### 2.1 Simple demo(only for a try)

Create a python file(G:\Project\intelligent-guide-dog\Code\Flask\main.py):

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'

```

Then set the environment variable for PowerShell(*make sure you are using PowerShell or the commend will be different*): 

*And make sure your PowerShell location is in the same directory level as main.py, just like "G:\Project\intelligent-guide-dog\Code\Flask\main.py".*

*Or you can use absolute paths instead of relative paths.*

```powershell
$env:FLASK_APP = "main.py"
```

Run it:

```powershell
python -m flask run
```

The default server will run on **http://127.0.0.1:5000**, just visit the URL on browser, you will find "Hello, World".



**By the way, if you want your web server can be visited publicly, you should add "--host=0.0.0.0", just like:**

```powershell
python -m flask run --host=0.0.0.0
```

### 2.2 Router

We use router() to combine function to URL:

```python
@app.route('/')
def index():
    return 'Index Page'


@app.route('/author')
def author():
    return 'Johnson Liu'
```

#### Variable rule

Variables can be added to a URL by marking a part or URL as <variable_name>, the tagged portion will be passed as keyword argument to the function.

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is {}'.format(username)
```

#### '/' or not

The URL for projects has a slash at the end, like a folder. When you access it, Flask automatically redirects you, adding a trailing slash.

The URL about has no trailing slash and looks like a file. If you access it with a trailing slash, you get a 404 error.

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

#### url_for()

The url_for() function constructs a URL for the specified function, taking the name of the function as the first argument. It can take any number of keyword arguments, each corresponding to a variable in the URL.

```python
from flask import Flask, escape, url_for

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


with app.test_request_context():
    print(url_for('index'))
    print(url_for('author', next='/'))
    print(url_for('show_user_profile', username='Johnson'))

```

```powershell
/
/author?next=/
/user/Johnson
```

#### HTTP method

We use different method in HTTP to deal with URL(Such as Get, Post......).

```python
from flask import request

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return index()
    else:
        return 'You should use Post method.'
```

