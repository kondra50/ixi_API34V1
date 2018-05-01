from OMNIFY import  models
from flask import jsonify
from flask_restful import Resource,reqparse,abort


class PartMismatch(Resource):
    def get(self):
        mydict=models.PartMitmatch()
        return jsonify(Mismatched=mydict)