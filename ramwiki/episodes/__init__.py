from flask import Blueprint

episodes = Blueprint (
    'episodes',
    __name__,
    template_folder='templates'
)