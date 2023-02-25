#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/c/<text>')
def c(text):
    """ display C followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
