from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import simplejson as json
import random,string
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
#from lxml import etree, objectify
Base = declarative_base()
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')

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
class Users(Base):
    __tablename__ = 'XXFUSR'

    USER_NAME = Column(String(250), primary_key=True, nullable=False)
    GROUP_NAME = Column(String(250), nullable=False)
    USER_PASSWORD =Column(String(250), nullable=False)
    FIRST_NAME = Column(String(250),  nullable=False)
    LAST_NAME = Column(String(250), nullable=False)
    USER_ID = Column(String(250), nullable=False)

    #Add add a decorator property to serialize data from the database

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'USER_NAME': self.USER_NAME,
            'GROUP_NAME': self.GROUP_NAME,
           'USER_PASSWORD' : self.USER_PASSWORD,
           'FIRST_NAME' : self.FIRST_NAME,
           'LAST_NAME' : self.LAST_NAME,
           'USER_ID' : self.USER_ID
       }
class Logs(Base):
    __tablename__ = 'ALFTD'

    RECNUM = Column(DECIMAL, primary_key=True, nullable=False)
    PROGRAM_ID = Column(String(250), nullable=False)
    TABLE_NAME =Column(String(250), nullable=False)
    OPERATOR_ID = Column(String(250),  nullable=False)
    FIRST_NAME = Column(String(250), nullable=False)
    LAST_NAME = Column(String(250), nullable=False)

    #Add add a decorator property to serialize data from the database

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'RECNUM': json.dumps(self.RECNUM),
           'PROGRAM_ID': self.PROGRAM_ID,
           'TABLE_NAME' : self.TABLE_NAME,
           'OPERATOR_ID' : self.OPERATOR_ID,
           'FIRST_NAME' : self.FIRST_NAME,
           'LAST_NAME' : self.LAST_NAME
       }

class Icfpm(Base):
    __tablename__ = 'ICFPM'

    PART_ID = Column(String(250), primary_key=True, nullable=False)
    ICFPM_USER_16 = Column(String(250), nullable=False)
    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       	   'PART_ID': self.PART_ID,
           'ICFPM_USER_16': self.ICFPM_USER_16,
       }

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
    	s = Serializer(secret_key, expires_in = expiration)
    	return s.dumps({'id': self.id })

    @staticmethod
    def verify_auth_token(token):
    	s = Serializer(secret_key)
    	try:
    		data = s.loads(token)
    	except SignatureExpired:
    		#Valid Token, but expired
    		return None
    	except BadSignature:
    		#Invalid Token
    		return None
    	user_id = data['id']
    	return user_id
class Tempo(object):
    """
    Class for temporary table used to process data coming from xlsx
    @param Base Declarative Base
    """
    # TODO: make it completely temporary
    __tablename__ = 'tempo'
    __table_args__ = {'prefixes': ['TEMPORARY']}

    RECNUM = Column(DECIMAL, primary_key=True, nullable=False)
    PROGRAM_ID = Column(String(250), nullable=False)
    TABLE_NAME =Column(String(250), nullable=False)

# class Spjobsinfo():
#     try:
#      PART_ID='10369ww1'
#      USER_NAME='MNAFISI'
#      cursor = connection.cursor()
#     #cursor.execute("select * from JCFJM where PART_ID='P003415'")
#     #cursor.callproc("Admin_EPROM_GETJOBINFO", ['107906','MNAFISI',PART_ID,PART_DESC,MFG_DATE,SHELF_LIFE,CTYPE,HasAccess,NOU,PPJ,Part_Programmed,ERRCODE])
#     #args=['107906','MNAFISI']
#     #cursor.callproc("Admin_EPROM_GETJOBINFOtest",['107906','MNAFISI'])
#      cursor.callproc('[Admin_EPROM_GETJOBINFO_API]',[PART_ID,USER_NAME])
#      @property
#      def serialize(cursor):
#         return {
#              "PART_ID": cursor[0],
#              "PART_DESC": cursor[1],
#              "MFG_DATE":cursor[2],
#              "SHELF_LIFE":cursor[3],
#              "CTYPE":cursor[4],
#              "HasAccess":cursor[5],
#              "NOU":cursor[6],
#              "PPJ":cursor[7],
#              "Part_Programmed":cursor[8],
#              "ERRCODE":cursor[9]
#      }
#         #print(row['JOB_ID'])
#
#     #cursor.close()
#     #connection.commit()
#     finally:
#         connection.close()


Base.metadata.create_all(engine)