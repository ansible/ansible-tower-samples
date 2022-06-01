import json
from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''



# FLASK_APP=log flask run -h 0.0.0.0 -p 8080
