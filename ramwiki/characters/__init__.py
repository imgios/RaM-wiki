from flask import Blueprint, render_template
from .manager import CharacterManager
from py2neo import Node
from ..utilities import getEntityCount

characters = Blueprint(
    'characters',
    __name__,
    template_folder='templates'
)

@characters.route('/')
def index():
    characterManager = CharacterManager()
    characters = []
    for x in range(1, 4):
        result = characterManager.getByNumber(x)
        character = result['data'][0]['c'] # Node result
        characters.append({
            "image": character['image'],
            "name": character['name'],
            "status": character['status'],
            "species": character['species']
        })

    return render_template('characters/index.html',
        number_of_characters=getEntityCount(characterManager.graph, 'c'), # testing purposed, must be changed
        characters = characters) # testing purposed, must be changed