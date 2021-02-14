from flask import Blueprint
from pathlib import Path

blueprint = Blueprint(
    'api_blueprint',
    __name__,
    url_prefix='/api',
    template_folder='templates',
    static_folder=str(Path(Path(__file__).parent.parent, "static"))
)

