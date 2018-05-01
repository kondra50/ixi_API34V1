from sqlalchemy import Column, Integer, String, DECIMAL,DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from cubes.tutorial.sql import  create_table_from_csv
from cubes import Workspace
import simplejson as json
import random,string
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
#from lxml import etree, objectify
Base = declarative_base()
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
# workspace = Workspace(config="slicer.ini")
# workspace.import_model("model1.json")
# browser = workspace.browser("ibrd_balance")

#engine = create_engine('sqlite:///data.sqlite')



# class Cube():
#     create_table_from_csv(engine,
#                       "data1.csv",
#                        table_name="ibrd_balance",
#                       fields=[
#                              ("category", "string"),
#                              ("category_label", "string"),
#                             ("subcategory", "string"),
#                              ("subcategory_label", "string"),
#                              ("line_item", "string"),
#                              ("year", "integer"),
#                              ("amount", "integer")],
#                      create_id=True
#                  )
#     def rec_count(self):
#         result = browser.aggregate()
#         result.summary["record_count"]
#         return result.summary["record_count"]

#engine = create_engine('mssql+pymssql://syspy:Welcome2015@192.168.3.145:1433/ESILOCAL')
connection = engine.raw_connection()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
class Sofom(Base):
    __tablename__ = 'SOFOM'

    SO_ID = Column(String(250), primary_key=True, nullable=False)
    SO_TYPE = Column(String(250), nullable=False)
    CUSTOMER_ID =Column(String(250), nullable=False)
    SHIP_TO_CUST = Column(String(250),  nullable=False)
    E_MAIL = Column(String(250), nullable=False)
    #Add add a decorator property to serialize data from the database

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       		'SO_ID': self.SO_ID,
           'SO_TYPE': self.SO_TYPE,
           'CUSTOMER_ID' : self.CUSTOMER_ID,
           'SHIP_TO_CUST' : self.SHIP_TO_CUST,
           'E_MAIL' : self.E_MAIL
       }

class KPI(Base):
    __tablename__ = 'IXI_KPI_BACKLOG_del'
    RECNUM = Column(Integer, primary_key=True, nullable=False)
    KPI = Column(String(250), nullable=False)
    VALUE =Column(DECIMAL, nullable=False)
    MONTH = Column(Integer,  nullable=False)
    YEAR = Column(Integer, nullable=False)
    DATE_TIME = Column(DATETIME, nullable=False)
    #Add add a decorator property to serialize data from the database

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'KPI': self.KPI,
           'VALUE': (self.VALUE),
           'MONTH' : self.MONTH,
           'YEAR' : self.YEAR,
           'DATE_TIME' : self.DATE_TIME
       }




Base.metadata.create_all(engine)