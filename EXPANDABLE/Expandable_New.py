from flask import  jsonify
from flask_restful import Resource,reqparse
from EXPANDABLE.model import LoadJobs
from SECURITY import  auth0middleware
from IXI_API_app import  Api
class jobs(Resource):

    # @Api.route('/users')

    def get(self):
        try:
         parser = reqparse.RequestParser()
         parser.add_argument('partid',required=False)
         parser.add_argument('jobstatus',required=False)
         args = parser.parse_args()
         partid = args['partid']
         status = args['jobstatus']
         list=LoadJobs(partid,status)
         return jsonify(Jobs=list)

        except Exception as e:
          return e






"""
@api {get} /api/exp/jobs?partid=P041746&jobstatus=c   jobs
@apiName jobs
@apiGroup Expandable
@apiVersion 0.1.0

@apiParam {String}  partid Expandable PART_ID
@apiParam {String}  jobstatus Expandable JOB STATUS


@apiSuccess {String} DATE_LAST_UPDT
@apiSuccess {String} JOB_ID
@apiSuccess {String} JOB_STATUS
@apiSuccess {String} JOB_TYPE
@apiSuccess {String} PART_ID



@apiSuccessExample Success-Response:
HTTP/1.1 200 OK
"Jobs": [
    {
      "DATE_LAST_UPDT": "Mon, 01 Aug 2011 00:00:00 GMT",
      "JOB_ID": "100002  ",
      "JOB_STATUS": "C",
      "JOB_TYPE": "S",
      "PART_ID": "P003284"
    },}
"""