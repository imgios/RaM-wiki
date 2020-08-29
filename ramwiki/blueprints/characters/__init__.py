from flask import Blueprint, render_template

characters = Blueprint(
    'characters',
    __name__,
    template_folder='templates'
)

@characters.route('/')
def index():
    return render_template('characters/index.html',
        number_of_characters="1", # testing purposed, must be changed
        characters = [{"name":"Test", "status":"alive", "species":"ai"},{"name":"Test2", "status":"alive", "species":"ai"},{"name":"Test3", "status":"alive", "species":"ai"}]) # testing purposed, must be changed