from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

# New route for the /time path
@app.route('/time')
def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)