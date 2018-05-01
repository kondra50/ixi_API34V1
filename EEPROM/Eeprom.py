from flask import jsonify
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from EEPROM.spobj import Spjobsinfo,Splogininfo, LoadPart
from SECURITY.mysecurity import  auth
from models import Base

#from flask_httpauth import HTTPBasicAuth
#auth= HTTPBasicAuth()
mylst=[]
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
connection = engine.raw_connection()


def updateJobInfo(jobid,machin_name,cartridge_id,exp_date,username):
   try:
      myobj=Spjobsinfo
      x=myobj.Update(jobid,machin_name,cartridge_id,exp_date,username)
      return x
      #return jsonify({"Error":"Internal Occured in database"}),502
      #return jsonify(myobj.Update(jobid,machin_name,cartridge_id,exp_date,username))
   except:
       return jsonify({"Error":"Internal Occured in database"}),502

def updateRFID(jobid,machin_name,cartridge_id,serialnumber,username):
   try:
      myobj=Spjobsinfo
      x=myobj.UpdateRFID(jobid,machin_name,cartridge_id,serialnumber,username)
      return x
      #return jsonify({"Error":"Internal Occured in database"}),502
      #return jsonify(myobj.Update(jobid,machin_name,cartridge_id,exp_date,username))
   except:
       return jsonify({"Error":"Internal Occured in database"}),502

def getAllParts():

    # lst=[]
    # for i in parts:
    try:
      return LoadPart()
      print("koskos")
     # parts =LoadPart()
     # print(parts[0].__dict__)
     # print(parts[0].serialize)
     # json_string = json.dumps([part.__dict__ for part in parts])
    except:
        print("kos")
    #     print(i.serialize(i))
    #return json.dumps(parts)
    #return jsonify(Users=[i.serialize for i in users])
     #s=(i.serialize for i in parts)
     #return jsonify(PartInfo=(i.serialize for i in parts))
########################################                                 ONE


########################################                                 TWO




class parts(Resource):
    #decorators = [auth.login_required]
    def get(self):
        mydict=getAllParts()
        return jsonify(partlist=mydict)

class logininfo(Resource):
    #decorators = [auth.login_required]
    def get(self):
        try:
         parser = reqparse.RequestParser()
         parser.add_argument('ldapuser',required=True,help="username cannot be blank!")
         args = parser.parse_args()
         ldapuser = args['ldapuser']
         myobj=Splogininfo.Load(Splogininfo,ldapuser)
        except:
          return jsonify({"Error":"Internal Occured in database"}),502
         #return jsonify({"Error":"Internal Occured in database"}),502
        if myobj.USERNAME!=('NA',):
              return jsonify(Logininfo=myobj.serialize(myobj))
        else:
            response = jsonify({'code': 404,'error': 'UserNotFound'})
            response.status_code = 404
            return response



class jobinfo(Resource):
    #decorators = [auth.login_required]
    def get(self):
        try:
         parser = reqparse.RequestParser()
         parser.add_argument('username',required=True,help="username cannot be blank!")
         parser.add_argument('jobid',required=True,help="jobid cannot be blank!")
         args = parser.parse_args()
         username = args['username']
         jobid = args['jobid']
         myobj=Spjobsinfo.Load(Spjobsinfo,jobid,username)
         if myobj.ERRCODE==('1',):
             response = jsonify({'code': 404,'error': 'JobNotFound'})
             response.status_code = 404
             return response
         elif  myobj.ERRCODE==('2',):
             response = jsonify({'code': 404,'error': 'JobIsClosed'})
             response.status_code = 404
             return response
         elif myobj.ERRCODE==('0',):
             return jsonify(Jobininfo=myobj.serialize(myobj))


         #return myobj.ERRCODE
         #return getJobsinfo(jobid,username)
         #return username
         #myobj=Spjobsinfo.Load(Spjobsinfo,id,username)
         #return jsonify({"Error":"Internal Occured in database"}),502
         #return jsonify(Jobsinfo=myobj.serialize(myobj))
        except Exception as e:
          return e
         #return jsonify({"Error":"Internal Occured in database"}),502
    def put(self):
         parser = reqparse.RequestParser()
         parser.add_argument('jobid',required=True,help="jobid cannot be blank!")
         parser.add_argument('machinname',required=True,help="machinname cannot be blank!")
         parser.add_argument('cartridgeid',required=True,help="cartridgeid cannot be blank!")
         parser.add_argument('expdate',required=True,help="expdate cannot be blank!")
         parser.add_argument('username',required=True,help="username cannot be blank!")
         args = parser.parse_args()
         jobid = args['jobid']
         machinname = args['machinname']
         cartridgeid = args['cartridgeid']
         expdate = args['expdate']
         username = args['username']
         try:
              x=updateJobInfo(jobid,machinname,cartridgeid,expdate,username)
              if len(x)==1: # there is error
                 response = jsonify({'code': 404,'error': x['ERROR']})
                 response.status_code = 404
                 return response
              if x['PP_UPDATED']==0:
                response = jsonify({'code': 404,'error': 'JobNotFound'})
                response.status_code = 404
                return response
              return jsonify(updated=x)

         except  Exception as e:
              print (e)
         #return res[1]

class rfid(Resource):
 def put(self):
         parser = reqparse.RequestParser()
         parser.add_argument('jobid',required=True,help="jobid cannot be blank!")
         parser.add_argument('machinname',required=True,help="machinname cannot be blank!")
         parser.add_argument('cartridgeid',required=True,help="cartridgeid cannot be blank!")
         parser.add_argument('serialnumber',required=True,help="serialnumber cannot be blank!")
         parser.add_argument('username',required=True,help="username cannot be blank!")
         args = parser.parse_args()
         jobid = args['jobid']
         machinname = args['machinname']
         cartridgeid = args['cartridgeid']
         serialnumber = args['serialnumber']
         username = args['username']
         try:
              x=updateRFID(jobid,machinname,cartridgeid,serialnumber,username)
              #print(len(x));
              if len(x)==1: # there is error
                 response = jsonify({'code': 404,'error': x['ERROR']})
                 response.status_code = 404
                 return response
              if x['PP_UPDATED']==0:
                response = jsonify({'code': 404,'error': 'JobNotFound'})
                response.status_code = 404
                return response
              if x['SN_UPDATED']==0:
                response = jsonify({'code': 404,'error': 'SN did not update to be tracked'})
                response.status_code = 404
                return response
              return jsonify(updated=x)

         except  Exception as e:
              print (e)



# def getAllParts():
#    parts = session.query(Icfpm).filter(Icfpm.ICFPM_USER_16 != '')
#    return jsonify(Parts=[i.serialize for i in parts])
#
# def getPartsjson():
#    parts = session.query(Icfpm).filter(Icfpm.ICFPM_USER_16 != '')
#    return jsonify(Parts=[i.serialize for i in parts])
#
# def getPartsxml():
#    parts = session.query(Icfpm).all()
#    dict= [i.serialize for i in parts]
#    dom = parseString(dicttoxml(dict))
#    return  Response(dicttoxml(dict) , mimetype='text/xml')

def getJobsinfo(id,username):
   try:

      myobj=Spjobsinfo.Load(Spjobsinfo,id,username)
      return jsonify(Jobsinfo=myobj.serialize(myobj))
   except:
       return jsonify({"Error":"Internal Occured in database"}),502

def getLoginInfo(ldapuser):
   try:

      myobj=Splogininfo.Load(Splogininfo,ldapuser)
      #return jsonify({"Error":"Internal Occured in database"}),502
      return jsonify(Logininfo=myobj.serialize(myobj))
   except:
       return jsonify({"Error":"Internal Occured in database"}),502














"""
@api {get} /api/epr/logininfo?ldapuser=mehrdad.nafisi  User's login
@apiSampleRequest http://192.168.3.146:8090/api/epr/logininfo
@apiName GetLoginInfo
@apiGroup EEPROM
@apiVersion 0.1.0


@apiParam {String}  ldapuser ldap user id (firtsname.lastname)

@apiSuccess {Boolean} ACCESS    Access to write data back to Expandable.
@apiSuccess {String} GROUP_NAME  Group Name of the User.
@apiSuccess {String} USERNAME   Expandable user name of the User.
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Logininfo": {
    "ACCESS": "0",
    "GROUP_NAME": "SYSADMIN",
    "USERNAME": "MNAFISS"
  }
}

@apiError UserNotFound The id of the User was not found.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"code": 404,
"error": "UserNotFound"
}
"""

########################################                                 THREE
"""
@api {get} /api/epr/parts  PARTS having REFERENCE CATALOG
@apiSampleRequest http://192.168.3.146:8090/api/epr/parts
@apiName GetPart
@apiGroup EEPROM
@apiVersion 0.1.0
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "partlist": [
    {
      "ICFPM_USER_16": "(Reference Catalog #400083)",
      "PART_ID": "P040447"
    },
    {
      "ICFPM_USER_16": "(Reference Catalog #400084)",
      "PART_ID": "P040448"
    },
    {
      "ICFPM_USER_16": "(Reference Catalog #400086)",
      "PART_ID": "P040449"
    },
    {
      "ICFPM_USER_16": "(Reference Catalog #400088)",
      "PART_ID": "P040579"
    },
    {
      "ICFPM_USER_16": "(Reference Catalog #400089)",
      "PART_ID": "P040580"
    },
    {
      "ICFPM_USER_16": "(Reference Catalog #400090)",
      "PART_ID": "P040581"
    }
  ]
}


@apiSuccess {String} PART_ID  Part ID.
@apiSuccess {String} ICFPM_USER_16   REFERENCE CATALOG .

"""


########################################                                 FOUR
"""
@api {get} /api/epr/jobinfo?jobid=102840&username=MNAFISI  Job Information
@apiSampleRequest http://192.168.3.146:8090/api/epr/jobinfo
@apiName GetJobInfo
@apiGroup EEPROM
@apiVersion 0.1.0


@apiParam {String}  jobid Expandable JOB_ID
@apiParam {String}  username Expandable userId ()

@apiSuccess {String} PART_ID    Expandable PART_ID.
@apiSuccess {String} PART_DESC  Expandable PART Description.
@apiSuccess {DATE} MFG_DATE  Expandable Manufactering date.
@apiSuccess {Integer} SHELF_LIFE  SHELF_LIFE in day.
@apiSuccess {String} CTYPE   Expandable CTYPE.
@apiSuccess {Boolean} HasAccess   If user has access to update back expandable.
@apiSuccess {Integer} NOU   Number of unit.
@apiSuccess {Integer} PPJ   Number of unit.
@apiSuccess {Integer} Part_Programmed   Number of part proggramed.
@apiSuccess {Integer} ERRCODE   error number.
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Jobininfo": {
    "CTYPE": "",
    "ERRCODE": "0",
    "HasAccess": "1",
    "MFG_DATE": "2013-02-27",
    "NOU": "0",
    "PART_DESC": "Assy, Lysis Chamber, Cleaned, RapidHIT",
    "PART_ID": "P038735",
    "PPJ": "59",
    "Part_Programmed": "1",
    "SHELF_LIFE": "0"
  }
}


@apiError JobNotFound The Jobid was not found.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"code": 404,
"error": "JobNotFound"
}

@apiError JobisClose The Jobid is closed.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"code": 404,
"error": "JobisClosed"
}
"""

########################################                                 FIFTH
"""
@api {put} /api/epr/jobinfo?jobid=102840&username=mnafisi&machinname=test&cartridgeid=123&expdate=12/12/2016 Job - Update  Part_Programmed and EXP date
@apiName UpdateJobInfo
@apiGroup EEPROM
@apiVersion 0.1.0


@apiParam {String}  jobid Expandable JOB_ID
@apiParam {String}  username Expandable userId
@apiParam {String}  machinname host of the Exe file
@apiParam {String}  cartridgeid  CARTRIDGE ID
@apiParam {Date}  expdate  new EXP Date to put in


@apiSuccess {Boolean} EXPDATE_UPDATE    Expiration date is updated.
@apiSuccess {Integer} PART_PROGRAMMED   number of Part Programmed.
@apiSuccess {Boolean} PP_UPDATED  Part Programmed is updated.
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "updated": {
    "EXPDATE_UPDATED": 1,
    "PART_PROGRAMMED": 2,
    "PP_UPDATED": 1
  }
}



@apiError JobNotFound The Jobid was not found.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"code": 404,
"error": "JobNotFound"
}

"""

########################################                                 SIXTH
"""
@api {put} /api/rfid/jobinfo?jobid=102840&username=mnafisi&machinname=test&cartridgeid=123&serialnumber=4563 Job - Update  Part_Programmed and keep SN tracable in Expandable
@apiName UpdateRFID
@apiGroup RFID
@apiVersion 0.1.0


@apiParam {String}  jobid Expandable JOB_ID
@apiParam {String}  username Expandable userId
@apiParam {String}  machinname host of the Exe file
@apiParam {String}  cartridgeid  CARTRIDGE ID
@apiParam {Integer}  serialnumber  Expandable Serial Number


@apiSuccess {Boolean} SN_UPDATED    SN is taken care of by Expandable.
@apiSuccess {Integer} PART_PROGRAMMED   number of Part Programmed.
@apiSuccess {Boolean} PP_UPDATED  Part Programmed is updated.
@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "updated": {
    "SN_UPDATED": 1,
    "PART_PROGRAMMED": 2,
    "PP_UPDATED": 1
  }
}



@apiError JobNotFound The Jobid was not found.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"code": 404,
"error": "JobNotFound"
}

@apiError SN did not update to be tracked
@apiErrorExample Error-Response:
HTTP/1.1 404 Error in SN update
{
"code": 404,
"error": "SN did not update"
}


"""