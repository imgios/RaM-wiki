import os
from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)

# a simple page that shows the status
@app.route('/status')
def hello():
    return 'Running!'