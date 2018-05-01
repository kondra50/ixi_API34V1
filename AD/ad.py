"""
@api {get} /api/ad/authenticate?username=mehrdad.nafisi&password=mypass  Authenticate user
@apiSampleRequest http://192.168.3.146:8090/api/ad/authenticate?username=mehrdad.nafisi&password=mypass
@apiName ADauthenticated
@apiGroup Active Directory
@apiVersion 0.1.0


@apiParam {String}  username  Windows username
@apiParam {String}  password  Windows password

@apiSuccess {String} Authenticate    Authentication status.

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Result": {
    "Authenticate": "Successful"
  }
}}

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Result": {
    "Authenticate": "InvalidCredentials"
  }
}


"""



from flask import jsonify
from flask_restful import Resource,reqparse
from AD.model import  CheckAD
class Authenticate(Resource):
    def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument('username',required=True,help="username cannot be blank!")
         parser.add_argument('password',required=True,help="password cannot be blank!")
         args = parser.parse_args()
         username = args['username']
         password = args['password']
         try:
             res= CheckAD(username,password)
             return jsonify(Result=res)
             #return res
         except Exception as e:
             return (e)