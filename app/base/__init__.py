from flask import Blueprint
from pathlib import Path

blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder=str(Path(Path(__file__).parent.parent, "static"))
)

# print(blueprint.static_folder)
