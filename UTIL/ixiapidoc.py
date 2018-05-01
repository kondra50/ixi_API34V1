from flask_restful import Resource
from flask import Flask, request, jsonify , Response,render_template,send_from_directory
app = Flask(__name__)
class Showhelp(Resource):
    def get(self):
        return app.send_static_file('index.html')
        #return "koskos"