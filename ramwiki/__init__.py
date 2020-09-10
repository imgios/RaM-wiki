import os
from ramwiki.utilities import getConnection, getNodesCount, getRelationshipsCount, getEntityCount
from flask import Flask, render_template, redirect, url_for
from .characters import characters
from .episodes import episodes

app = Flask(__name__)
app.secret_key = os.urandom(24)

# TO-DO: register blueprints
app.register_blueprint(characters, url_prefix='/characters')
app.register_blueprint(episodes, url_prefix='/episodes')

# (?) TEMP: App index redirect to the status page
@app.route('/')
def index():
    return redirect(url_for('status'), code = 307)

# a simple page that shows the status
@app.route('/status')
def status():
    dbGraph = getConnection()
    nodesCount = getNodesCount(dbGraph)
    relsCount = getRelationshipsCount(dbGraph)
    entityCount = {
        "characters": getEntityCount(dbGraph, "c"),
        "episodes": getEntityCount(dbGraph, "e"),
        "locations": getEntityCount(dbGraph, "l"),
    }

    return render_template('status.html',
        number_of_characters=entityCount["characters"],
        number_of_episodes=entityCount["episodes"],
        number_of_locations=entityCount["locations"],
        number_of_relationships=relsCount,
        number_of_nodes=nodesCount)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404