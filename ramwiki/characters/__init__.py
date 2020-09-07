from flask import Blueprint, render_template
from .manager import CharacterManager
from py2neo import Node
from ..utilities import getEntityCount
import random

characters = Blueprint(
    'characters',
    __name__,
    template_folder='templates'
)

@characters.route('/')
def index():
    characterManager = CharacterManager()
    totalCharacters = getEntityCount(characterManager.graph, 'c') # Number of Characters nodes in the database
    characters = [] # Characters retrieved
    # Retrieving characters from the database with a random value as character number
    i = 0
    while i < 3:
        characterNumber = random.randint(1, totalCharacters)
        result = characterManager.getByNumber(characterNumber) # Retrieve character by random id from database
        character = result['data'][0]['c'] # Node result
        characters.append({
            "image": character['image'],
            "name": character['name'],
            "status": character['status'],
            "species": character['species'],
            "location": character['location'],
            "actedIn": len(character['episode'])
        })
        i+=1

    return render_template('characters/index.html',
        number_of_characters = totalCharacters,
        characters = characters)
