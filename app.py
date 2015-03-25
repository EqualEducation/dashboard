from flask import Flask
from flask import render_template
from pymongo import Connection
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
connectionName= 'production-db-d1.meteor.io:27017/ee_survey_meteor_com'
MONGODB_PORT = 27017
#DBS_NAME = 'donorschoose'
#COLLECTION_NAME = 'projects'
#FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}
DBS_NAME = 'EqualEducation'
COLLECTION_NAME = 'schools'
FIELDS = {'name': True, 'type': True, 'Suburb': True,'District':True,'EMIS':True,'male':True,'female':True,'total':True,'teachers':True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    #connection = Connection(MONGODB_HOST, MONGODB_PORT)
    #collection = connection[DBS_NAME][COLLECTION_NAME]
    client = MongoClient(MONGODB_HOST,MONGODB_PORT)
    db = client[DBS_NAME]
    collection = db[COLLECTION_NAME]
    projects = collection.find(fields=FIELDS, limit=50000)
    #projects=collection.find()
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    #connection.disconnect()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)