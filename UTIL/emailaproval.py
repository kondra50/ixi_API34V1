from flask import Flask, request, jsonify , Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Sofom,Users,Logs,Icfpm
from flask_httpauth import HTTPBasicAuth
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import time
import json
from flask_restful import Resource
# from ssl import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('yourserver.key')
# context.use_certificate_file('yourserver.crt')

auth= HTTPBasicAuth()
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/FLORENCE')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)



@app.route("/api/v0/approvals/", methods = ['GET', 'POST', 'DELETE'])
@auth.login_required
def Approvals():
  if request.method == 'GET':
    #Call the method to Get all of the puppies
    return getApprovals()
    #return "koskos"
  elif request.method == 'POST':
    name = request.args.get('name', '')
    description = request.args.get('description', '')
    #return "koskos"
    return writeApprovals(name,description)
    #Call the method to make a new puppy
    #print "Making a New puppy"
  elif request.method == 'DELETE':
    with open('test.json') as f:
     data = json.load(f)
     # data["aprovals"].append(a_dict)
     data["aprovals"].clear()
     #data['ADDED_KEY'] = 'ADDED_VALUE2'
     with open('test.json', 'w') as f:
      json.dump(data, f)
     return "The cash in Empty"

# @app.route("/api/v0/approvals/", methods = ['DELETE'])
# def deleteApprovals():
#     with open('test.json') as f:
#      data = json.load(f)
#      # data["aprovals"].append(a_dict)
#      data["aprovals"].clear()
#      #data['ADDED_KEY'] = 'ADDED_VALUE2'
#      with open('test.json', 'w') as f:
#       json.dump(data, f)
#      return "The cash in Empty"
mydict={}
def getApprovals():
    with open('test.json') as json_data:
        d = json.load(json_data)
        json_data.close()
    return jsonify(d)

def writeApprovals(name,description):
    #with open('approvals.json', 'a') as outfile:
        #json.dump("name:"+ name +" , description:" + description , outfile)
    a_dict = {
    "name": name,
    "description": description,
     }
    with open('test.json') as f:
     data = json.load(f)
     data["aprovals"].append(a_dict)
     #data['ADDED_KEY'] = 'ADDED_VALUE2'
     with open('test.json', 'w') as f:
      json.dump(data, f)


    # with open(json_file, 'w') as json_file:
    # json.dump(json_decoded, json_file)
    # file = open("approvals.txt", "a")
    # file.write("'name':"+ name +" , 'description':" + description +"\n" )
    # file.close()
    return "Approval is writen for name %s" % name + " description%s"  % description , 201



@auth.verify_password
def verify_password(username,password):
    if username=='api' and password=='Welcome2015':
     return True
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8087)