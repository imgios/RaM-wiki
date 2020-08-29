from flask import Blueprint, render_template

characters = Blueprint(
    'characters',
    __name__,
    template_folder='templates'
)

@characters.route('/')
def index():
    return render_template('characters/index.html')