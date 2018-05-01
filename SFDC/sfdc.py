from SFDC import models, dbmodels
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, abort
from flask.ext.jsonpify import jsonpify

class Opurtinity(Resource):
    def get(self):
        mydict=models.Opportunities()
        return jsonify(Oppurtinity=mydict)

class Pricebook(Resource):
    def get(self):
        mydict=models.PriceBooks()
        return jsonify(Pricebook=mydict)

class Product(Resource):


    def get(self):

        mydict=models.Products()
        return jsonify(Product=mydict)



class User(Resource):
    def get(self):
        mydict=models.Users()
        return jsonify(User=mydict)


class Account(Resource):
    def get(self):
        mydict = models.Accounts()
        return jsonify(Account=mydict)


class Case(Resource):
    def get(self):
        mydict=models.Cases()
        return jsonify(cases=mydict)

class Report(Resource):
    def get(self):
        mydict=models.Reports()
        return jsonify(Report=mydict)


class RunReport_Forecast_PIP(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('callback', required=False)
        args = parser.parse_args()
        callback = args['callback']
        mydict=models.Run_Forecast_PIP()
        #return mydict
        if (callback is None): return jsonify(ForecastPipeline=mydict)
        if (callback is not None): return jsonpify(ForecastPipeline=mydict)
class Run_Exp_SF4_Cleanup(Resource):
    def get(self):
        mydict=models.Run_Exp_SF4_Cleanup(self)
        #return mydict
        return jsonify(EXP4SFDC=mydict)

class SFDC_EXP_DESCREPENCY(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('callback', required=False)
            parser.add_argument('cached', required=True)
            args = parser.parse_args()
            callback = args['callback']
            iscached = args['cached']
            if iscached.lower()=='false':
                dbmodels.EXPUPDATE.CLEANSFDC7()
                SFrows=models.Run_Exp_SF4_Cleanup()
                for row in SFrows:
                 dbmodels.EXPUPDATE.FillSFDC7(row)

            mydict=dbmodels.EXPUPDATE.SFDC_EXP_DESCREPANCY()
            if callback is None: return jsonify(DESCREPENCIES=mydict)
            if callback is not None:
                resp = make_response(jsonpify(DESCREPENCIES=mydict))
                resp.headers['Access-Control-Allow-Origin'] = '*'
                return resp
        except Exception as e:
            return {"ERROR":str(e)}
class SOFOD(Resource):
    def get(self):
        mydict=models.SOFOD()
        return jsonify(EXP4SFDC=mydict)

class SOLUTION(Resource):
    def put(self):
        models.Craete_Solution()