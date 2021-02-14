from flask import jsonify, render_template, redirect, url_for, send_from_directory
import os
from pathlib import Path
from . import blueprint


@blueprint.route('/')
def route_default():
    return render_template('home.html')

@blueprint.route('/static/css/<path>')
def static_file(path):
    static_folder = os.path.join(Path(__file__).parent.parent, 'static', 'css')
    return send_from_directory(static_folder, path)


## Errors
@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
