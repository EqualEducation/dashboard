from flask import Flask
from flask import render_template
from pymongo import Connection
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

#MONGODB_HOST = 'localhost'
MONGODB_HOST = "mongodb://dashboard:dashboard@production-db-d1.meteor.io:27017/ee_survey_meteor_com"
#connectionName= 'production-db-d1.meteor.io:27017/ee_survey_meteor_com'
MONGODB_PORT = 27017
#DBS_NAME = 'donorschoose'
#COLLECTION_NAME = 'projects'
#FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}
DBS_NAME = 'ee_survey_meteor_com'
SCHOOL_COLLECTION_NAME = 'schools'
GRADES_COLLECTION_NAME='grades'
#FIELDS = {'schoolDetails': True,'schoolDetails.INSTITUTION_NAME':True,'_id':False}
SCHOOL_FIELDS = {'schoolDetails.INSTITUTION_NAME': True, 'schoolDetails.PROVINCE_NAME': True, 'schoolDetails.CLASSIFICATION': True,'schoolDetails.principalCooperative':True,'schoolDetails.DISTRICT_NAME':True,'schoolDetails.TOWN_OR_CITY':True,'schoolDetails.NEIMS_NUMBER':True,'schoolDetails.TELEPHONE_NO':True, '_id': False}
#FIELDS = {'name': True, 'type': True, 'Suburb': True,'District':True,'EMIS':True,'male':True,'female':True,'total':True,'teachers':True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():
    #connection = Connection(MONGODB_HOST, MONGODB_PORT)
    #collection = connection[DBS_NAME][COLLECTION_NAME]
    client = MongoClient(MONGODB_HOST,MONGODB_PORT)
    db = client[DBS_NAME]
    school_collection = db[SCHOOL_COLLECTION_NAME]
    schools = school_collection.find(fields=SCHOOL_FIELDS)
    grade_collection=db[GRADES_COLLECTION_NAME]
    grades=grade_collection.find()
    #projects=collection.find()
    json_schools = []
    for school in schools:
        school_id=school
        gradeInformation=grade_collection.find({"school_id":school_id})
        #print gradeInformation
        json_schools.append(school)
    json_schools = json.dumps(json_schools, default=json_util.default)
    #connection.disconnect()
    return json_schools

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)