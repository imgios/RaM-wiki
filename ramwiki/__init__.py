import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

# a simple page that shows the status
@app.route('/status')
def status():
    return render_template('status.html',
        number_of_characters='TO-DO',
        number_of_episodes='TO-DO',
        number_of_locations='TO-DO',
        number_of_relationships='TO-DO',
        number_of_nodes='TO-DO')