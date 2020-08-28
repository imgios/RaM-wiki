import os
from ramwiki.utilities import getConnection, getNodesCount, getRelationshipsCount
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

# TO-DO: register blueprints

# a simple page that shows the status
@app.route('/status')
def status():
    dbGraph = getConnection()
    nodesCount = getNodesCount(dbGraph)
    relsCount = getRelationshipsCount(dbGraph)

    return render_template('status.html',
        number_of_characters='TO-DO',
        number_of_episodes='TO-DO',
        number_of_locations='TO-DO',
        number_of_relationships=relsCount,
        number_of_nodes=nodesCount)