# handles the application routing
from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_article

#views

@main.route('/')
def index():
    """ view function that returns the index page and its data """
    sources = get_sources()
    return render_template('index.html') 