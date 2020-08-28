import os
import urllib.request
import json
from py2neo import Graph
from utilities import getConnection

# Estabilishing connection to the database
dbIstance = getConnection()

# Clean the entire graph
dbIstance.delete_all()

# Index on nodes
# TO-DO: Character composite index
# dbIstance.schema.create_index('Character', ['name', 'gender'])
dbIstance.schema.create_index('Episode', 'episode')
dbIstance.schema.create_index('Location', 'name')

# Initialize the graph
# Create Character nodes
charactersJsonUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/data/characters.json'
with urllib.request.urlopen(charactersJsonUrl) as url:
    charactersJson = json.loads(url.read().decode())

charactersScriptUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/cyphers/creation/create-characters.cyp'
with urllib.request.urlopen(charactersScriptUrl) as url:
    charactersInsert = url.read().decode()
dbIstance.run(charactersInsert, data=charactersJson)

# Create Episode nodes
episodesJsonUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/data/episodes.json'
with urllib.request.urlopen(episodesJsonUrl) as url:
    episodesJson = json.loads(url.read().decode())

episodesScriptUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/cyphers/creation/create-episodes.cyp'
with urllib.request.urlopen(episodesScriptUrl) as url:
    episodesInsert = url.read().decode()
dbIstance.run(episodesInsert, data=episodesJson)

# Create Location nodes
locationsJsonUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/data/locations.json'
with urllib.request.urlopen(locationsJsonUrl) as url:
    locationsJson = json.loads(url.read().decode())

locationsScriptUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/cyphers/creation/create-locations.cyp'
with urllib.request.urlopen(locationsScriptUrl) as url:
    locationsInsert = url.read().decode()
dbIstance.run(locationsInsert, data=locationsJson)

# Relationship APPEARS_IN between Characters and Episodes
appearsInScriptUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/cyphers/creation/relationship-appearsin.cyp'
with urllib.request.urlopen(appearsInScriptUrl) as url:
    appearsInScript = url.read().decode()
dbIstance.run(appearsInScript)

# Relationship LIVES_ON between Characters and Locations
livesOnScriptUrl = 'https://raw.githubusercontent.com/imgios/RaM-wiki/master/cyphers/creation/relationship-liveson.cyp'
with urllib.request.urlopen(livesOnScriptUrl) as url:
    livesOnScript = url.read().decode()
dbIstance.run(livesOnScript)