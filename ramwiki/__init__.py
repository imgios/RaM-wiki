import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

# a simple page that shows the status
@app.route('/status')
def status():
    return render_template('status.html')