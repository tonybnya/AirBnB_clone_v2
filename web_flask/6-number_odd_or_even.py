#!/usr/bin/python3
"""
This Python script starts a Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Displays Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Displays HBNB!'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    '''Displays "C" followed by the value of the text variable'''
    text = text.replace("_", " ")

    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ptext(text='is cool'):
    '''Displays "Python" followed by the value of the text variable'''
    text = text.replace("_", " ")

    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def numbern(n):
    '''Displays "n is a number" only if n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    '''
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberoddeven(n):
    '''
    Displays a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    '''
    evenodd = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenodd=evenodd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
