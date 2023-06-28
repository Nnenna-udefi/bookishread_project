#!/usr/bin/python3
"""script to run and debug app"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from web_flask.get_book import get_book_by_id
from web_flask.app import app


if __name__ == '__main__':
    app.run(debug=True)
