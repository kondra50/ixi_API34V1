from flask import Flask, request, jsonify , Response,g
from KPI.models import Base,KPI
from flask_restful import Resource,reqparse,abort
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def abort_if_kpi_doesnt_exist(kpis):
    if kpi not in kpis:
        abort(404, message="Todo {} doesn't exist".format(kpis))
    #return ("The requested data is not exist!".format(kpis)),404



class kpis(Resource):
    def get(self):
        return getAllKPI()

#@app.route("/")
# @app.route("/logs/", methods = ['GET', 'POST'])
# def getAllUsers():
#   if request.method == 'GET':
#      return getAllLogs()


class kpi(Resource):
    def get(self,kpicode):
        return getKPI(kpicode)

# class kpi(Resource):
#     def get(self):
#         return Cube.rec_count()

def getKPI(kpicode):
  parser = reqparse.RequestParser()
  parser.add_argument('month', type=int, help='Rate to charge for this resource')
  parser.add_argument('year', type=int, help='Rate to charge for this resource')
  args = parser.parse_args(strict=True)
  m=args.month
  y=args.year

  if ( m == None and  y == None ):
    print("joft khali")
    kpis = session.query(KPI).filter_by(KPI = kpicode).all()
    abort_if_kpi_doesnt_exist(kpis)
  elif not ( m == None or  y == None ):
    print("joft por")
    kpis = session.query(KPI).filter_by(KPI = kpicode,YEAR = args.year,MONTH = args.month).all()
    abort_if_kpi_doesnt_exist(kpis)
  elif (not (m==None)):
    print("month por")
    kpis = session.query(KPI).filter_by(KPI = kpicode,MONTH = args.month).all()
    abort_if_kpi_doesnt_exist(kpis)
  elif not (y==None):
    print("sal por")
    kpis = session.query(KPI).filter_by(KPI = kpicode,YEAR = args.year).all()
    abort_if_kpi_doesnt_exist(kpis)

  #kpis = session.query(KPI).filter_by(KPI = kpicode,MONTH=args.month).all()
  return jsonify(KPI=[i.serialize for i in kpis])
   #return m
def getAllKPI():
  parser = reqparse.RequestParser()
  parser.add_argument('month', type=int, help='Rate to charge for this resource')
  parser.add_argument('year', type=int, help='Rate to charge for this resource')
  args = parser.parse_args(strict=True)
  kpis = session.query(KPI).all()
  return jsonify(KPI=[i.serialize for i in kpis])