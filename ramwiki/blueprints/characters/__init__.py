from flask import Blueprint

characters = Blueprint(
    'characters',
    __name__,
    template_folder='templates'
)