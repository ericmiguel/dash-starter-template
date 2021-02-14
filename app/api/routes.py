from flask import jsonify, render_template, redirect, url_for, send_from_directory
import os
from pathlib import Path
from . import blueprint


@blueprint.route('/')
def route_default():
    return "API", 200

@blueprint.route('/static/css/<path>')
def static_file(path):
    static_folder = os.path.join(Path(__file__).parent.parent, 'static', 'css')
    return send_from_directory(static_folder, path)