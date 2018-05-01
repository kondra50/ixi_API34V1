from flask import jsonify, make_response
from flask_restful import Resource,reqparse
from ALM  import model
class UpdateALM(Resource):

 def get(self):
        try:
         parser = reqparse.RequestParser()
         parser.add_argument('recordtype',required=True)
         parser.add_argument('casenumber',required=True)
         parser.add_argument('serialnumber',required=True)
         parser.add_argument('custgui',required=True)
         parser.add_argument('ccsn',required=True)
         parser.add_argument('createdby',required=True)
         parser.add_argument('ownerid',required=True)
         parser.add_argument('subject',required=True)
         parser.add_argument('desc',required=True)
         parser.add_argument('module',required=True)
         parser.add_argument('primecart',required=True)
         parser.add_argument('cartridgelot',required=True)
         parser.add_argument('product', required=True)
         parser.add_argument('runlogname', required=True)
         parser.add_argument('fversion', required=True)
         parser.add_argument('runonpcart', required=True)
         parser.add_argument('customer', required=True)
         args = parser.parse_args()

         recordtype = args['recordtype']
         casenumber = args['casenumber']
         serialnumber = args['serialnumber']
         custgui = args['custgui']
         ccsn = args['ccsn']
         createdby = args['createdby']
         ownerid = args['ownerid']
         subject = args['subject']
         desc = args['desc']
         module = args['module']
         primecart = args['primecart']
         cartridgelot = args['cartridgelot']
         product = args['product']
         runlogname = args['runlogname']
         fversion = args['fversion']
         runonpcart = args['runonpcart']
         customer = args['customer']
         result=model.Update(recordtype,casenumber,serialnumber,custgui,ccsn,createdby,ownerid,subject,desc,module,primecart,cartridgelot,product,runlogname,fversion,runonpcart,customer)
         return jsonify(Result=result)

        except Exception as e:
         if (str(e)=="400: Bad Request"): return jsonify(error={"ERROR":"Fill all parameters as shown in documentation"})
         if (str(e)=="404: Not Found"): return jsonify(error={"Invalid RecordType":"select a valid RecordType"})
         return e





class Defectslist(Resource):

 def get(self):
        try:
         parser = reqparse.RequestParser()
         parser.add_argument('recordtype', required=True)
         parser.add_argument('casenumber', required=True)
         args = parser.parse_args()
         recordtype = args['recordtype']
         casenumber = args['casenumber']
         result=model.List(recordtype, casenumber)
         #return result
         return jsonify(Result=result)

        except Exception as e:
         if (str(e)=="400: Bad Request"): return jsonify(error={"ERROR":"Fill all parameters as shown in documentation"})
         if (str(e)=="404: Not Found"): return jsonify(error={"Invalid RecordType":"select a valid RecordType"})
         return {'kos':e}


class Htmltest(Resource):

  def get (self):

   try:
       return  make_response('<html lang="en"><head><body><h1>this is test</h1></body></head></html>')
       #return '<html lang="en"><head><body><h1>this is test</h1></body></head></html>'

   except Exception as e:

       return ''

"""
@api {get} /api/alm/sfdefect?recordtype=RHID&casenumber=354653&serialnumber=RH200-0046&custgui=a&ccsn=a&createdby=Customer+Service&ownerid=Customer+Service&subject=TEST+BY+MEHRDAD&desc=mydwsc&module=System&primecart=primecart&cartridgelot=cartridgelot New Defect
@apiSampleRequest http://192.168.3.146:8090/api/alm/sfdefect?recordtype=RHID&casenumber=354653&serialnumber=RH200-0046&custgui=a&ccsn=a&createdby=Customer+Service&ownerid=Customer+Service&subject=TEST+BY+MEHRDAD&desc=mydwsc&module=System&primecart=primecart&cartridgelot=cartridgelot
@apiName Defect Update
@apiGroup ALM
@apiVersion 0.1.0


@apiParam {String}  recordtype  RHID,RH
@apiParam {String}  casenumber
@apiParam {String}  serialnumber
@apiParam {String}  custgui     Custome GUI
@apiParam {String}  ccsn        Command Center Serial Number
@apiParam {String}  createdby
@apiParam {String}  ownerid
@apiParam {String}  subject
@apiParam {String}  desc
@apiParam {String}  module
@apiParam {String}  primecart    Runs On Prime
@apiParam {String}  cartridgelot Cartridge Lot



@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Result": {
    "ALM Defect Number": 2780,
    "Case Number": "354653",
    "CreartedBy": "Customer Service",
    "Subject": "TEST BY MEHRDAD",
    "Successfull": "The defect has been sent to RHID database!"
  }
}

@apiError RecordType The RecordType is invalid.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"Invalid RecordType": "select a valid RecordType"
}
"""


"""
@api {get} /api/alm/defect?recordtype=RHID&casenumber=122453  Defect Info
@apiSampleRequest http://192.168.3.146:8090/api/alm/defects?recordtype=RHID&casenumber=122453
@apiName Defect Info
@apiGroup ALM
@apiVersion 0.1.0


@apiParam {String}  recordtype  RHID,RH
@apiParam {String}  casenumber  RHID,RH

@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
{
  "Result": {
    "Defect Number": 2781,
    "Status": 1
  }
}

@apiError RecordType The RecordType is invalid.
@apiErrorExample Error-Response:
HTTP/1.1 404 Not Found
{
"Invalid RecordType": "select a valid RecordType"
}
"""