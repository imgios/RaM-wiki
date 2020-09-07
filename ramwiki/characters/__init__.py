from flask import Blueprint, render_template, request, jsonify
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
    """Character category index that shows three random character from the database,
    the number of characters stored and a search bar."""
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
            "number": character['no'],
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

@characters.route('/<int:characterNumber>')
def characterInfo(characterNumber):
    """Character page that shows in-depth details."""
    characterManager = CharacterManager()
    result = characterManager.getByNumber(characterNumber)['data']
    if len(result) > 0:
        character = result[0]['c'] # Character found
    else:
        character = None # Character not found
    
    return render_template('characters/characterInfo.html',
    character = character)

@characters.route('/search')
def searchCharacters():
    """Character search page that shows results based on the name given."""
    if 'name' in request.args:
        characterManager = CharacterManager()
        characterName = request.args.get('name')
        data = characterManager.getByName(characterName)
        if len(data) > 0:
            characters = [i for i in data['data']]
            results = []
            for character in characters:
                results.append({
                    'number': character['c']['no'],
                    'name': character['c']['name'],
                    'gender': character['c']['gender'],
                    'species': character['c']['species'],
                    'origin': character['c']['origin'],
                    'status': character['c']['status']
                })

            return render_template('characters/search.html',
            results = results)
        else:
            results = None
            return render_template('characters/search.html',
            results = results)
    else:
        results = None
        return render_template('characters/search.html',
        results = results)