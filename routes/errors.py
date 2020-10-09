from . import routes
from flask import render_template, redirect, url_for, current_app

@routes.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')
