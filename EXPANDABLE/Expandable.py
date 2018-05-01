import random
import string
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from flask import Flask, request, jsonify , Response,g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from EEPROM.Eeprom import  getJobsinfo,getLoginInfo,updateJobInfo
from models import Base, Sofom,Users,Logs, User,Icfpm
#from passlib.apps import custom_app_context as pwd_context
#from OpenSSL import SSL
#from flask.ext.autodoc import Autodoc
from flask_restful import Resource,reqparse
import time











































"""
@api {get} /api/exp/users  User information
@apiName GetUser
@apiGroup Expandable
@apiVersion 0.1.0

@apiSuccess {String} FIRST_NAME Firstname of the User.
@apiSuccess {String} GROUP_NAME  Group Name of the User.
@apiSuccess {String} LAST_NAME   last Name of the User.
@apiSuccess {String} USER_ID     User Id of the User.
@apiSuccess {String} USER_NAME   user  Name of the User.
@apiSuccess {String} GROUP_NAME  Group Name of the User.


@apiError UserNotFound The id of the User was not found.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
"""


auth= HTTPBasicAuth()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/FLORENCE')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
#auto = Autodoc(app)


class so(Resource):
    def get(self):
        return getAllSO()

class users(Resource):
    def get(self):
        return getAllUsers()

class parts(Resource):
    def get(self):
        return getAllParts()

#@app.route("/")
# @app.route("/logs/", methods = ['GET', 'POST'])
# def getAllUsers():
#   if request.method == 'GET':
#      return getAllLogs()






def getAllLogs():
  logs = session.query(Logs).all()
  return jsonify(Logs=[i.serialize for i in logs])

def getSO(id):
  so = session.query(Sofom).filter_by(id = id).one()
  return jsonify(puppy=so.serialize)





def getAllParts():
   parts = session.query(Icfpm).filter(Icfpm.ICFPM_USER_16 != '')
   return jsonify(Parts=[i.serialize for i in parts])

#@app.route("/api/v0/jobsinfo/<int:id>", methods = ['GET'])
#@auto.doc(groups=['jobsinfo', 'public', 'private'])
#@auth.login_required
def JobsInfoFunctionjson(id):
  #"""return information about job in json format"""
  if request.method == 'GET':
    username = request.args.get('username', '')
    return getJobsinfo(id,username)

#@app.route("/api/v0/logininfo/<string:ldapuser>", methods = ['GET'])
#@auto.doc(groups=['logininfo', 'public', 'private'])
#@auth.login_required
def LoginInfoFunctionjson(ldapuser):
 # """return Expandable user of a given LDAP user"""
  if request.method == 'GET':
    return getLoginInfo(ldapuser)


     # @JOB_ID nchar(8)
	# ,@MACHIN_NAME nvarchar(50)
	# ,@CARTRIDGE_ID nvarchar(50)
	# ,@EXP_DATE date
	# ,@USERNAME nvarchar(25)
@app.route("/api/v0/jobsinfo/", methods = ['POST'])
#@auth.login_required
def JobsInfoUpdateFunctionjson():
  if request.method == 'POST':
     jobid = request.args.get('jobid', '')
     machin_name = request.args.get('machin_name', '')
     cartridge_id = request.args.get('cartridge_id', '')
     exp_date = request.args.get('exp_date', '')
     username = request.args.get('username', '')
     return updateJobInfo(jobid,machin_name,cartridge_id,exp_date,username)

# @app.route("/delay")
# def delay():
#     time.sleep(10)
#     return "Waited for 10 Second"


class delay(Resource):
    def get(self):
        return {'hello': 'world2'}

def SOFunction():
  if request.method == 'GET':
    return getAllSO()


def getAllSO():
  puppies = session.query(Sofom).all()
  return jsonify(Puppies=[i.serialize for i in puppies])
  #return puppies.SO_ID

def getAllUsers():
  users = session.query(Users).all()
  #xml = dicttoxml(Users=[i.serialize for i in users])
  #return dicttoxml(jsonify(Users=[i.serialize for i in users]))
  return jsonify(Users=[i.serialize for i in users])


def generate_auth_token(self,expiration=600):
  s=Serializer(secret_key,expires_in=expiration)
  return s.dumps({'id':self.id})

@staticmethod
def verify_auth_token(token):
  s=Serializer(secret_key)
  try:
    data=s.loads(token)
  except SignatureExpired:
    return None
  except BadSignature:
    return  None
  user_id=data['id']
  return user_id

# @app.route("/api/v0/token", methods = ['GET'])
# def get_auth_token():
#   token=g.

@app.route("/api/v0/session", methods = ['POST'])
#@auth.login_required
def SessionFunction():
  if request.method == 'POST':
    name = request.args.get('name', '')
    g.user=name

@auth.verify_password
def verify_password(username_or_token, password):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True



@app.route('/token')
#@auto.doc(groups=['token', 'public', 'private'])
@auth.login_required
def get_auth_token():
    """Get The token which is needed to call all other apis"""
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

@app.route('/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print("missing arguments")
        #abort(400)

    if session.query(User).filter_by(username = username).first() is not None:
        print("existing user")
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'}), 200#, {'Location': url_for('get_user', id = user.id, _external = True)}

    user = User(username = username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'username': user.username }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/')
@app.route('/docs')
def public_doc():
    return auto.html(groups=['public'], title='EEPROM Documentation')


@app.route('/doc/private')
def private_doc():
    return auto.html(groups=['private'], title='EEPROM Documentation')



if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
   # app.run(host='0.0.0.0', port=8090)