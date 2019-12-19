#!flask/bin/python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__,
            static_url_path='',
            static_folder='../')
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/book/<int:id>')
def getBook(id):
    return "You want book with " + str(id)


if (__name__ == '__main__'):
    app.run(debug = True)


# **************************************
# NOTES
# **************************************

## Routing (URL Mapping)
# @app.route('/user', methods=['GET', 'POST'])

## Variable in rout (URL)
# @app.route('user/<username>')
# @app.route('user/<int:post_id>')

## Use the url_for() function to generate a url to a particular function
# @app.route('/')
# def index():
#     return 'index'

## somewhere else
# print(url_for(index))
## will print out /