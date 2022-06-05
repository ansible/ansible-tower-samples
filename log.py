#FROM GABE
import json
from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''

# create a py file on the controller server with the above. Then run it with the command below. 
# If flask is not installed, use pip3 to install.
# FLASK_APP=log flask run -h 0.0.0.0 -p 8080


#------------------------------------------------------------------------------------------------#
# FROM BEN
import json
from flask import Flask, escape, request
import logging
app = Flask(__name__)
logging.basicConfig(filename='tower_elk.log', level=logging.DEBUG)
@app.route('/', methods=['POST'])
def log():
    data = json.loads(request.data)
    print(data)
    return ''

# create a py file on the controller server with the above. Then run it with the command below. 
# If flask is not installed, use pip3 to install.
# FLASK_APP=log flask run -h 0.0.0.0 -p 8080


#-------------------------------------------------------------------------#
#Controller settings:
#Logging Aggregator = http://localhost
#Logging Aggregator Port = 8080
#Logging Aggregator Type = 
#Logging Aggregator Protocol = HTTPS/HHTP
#
#













