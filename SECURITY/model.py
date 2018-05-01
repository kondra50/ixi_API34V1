#from flask import Flask
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base,base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import random, string

#from flask_sqlalchemy import SQLAlchemy
#app = Flask(__name__)
Base = declarative_base()

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)


secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
auth= HTTPBasicAuth()
engine = create_engine('sqlite:///usersWithTokens.db', connect_args={'check_same_thread':False})



class User(Base):
    __tablename__ = 'user'
    username = Column(String(32), primary_key=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
    	s = Serializer(secret_key, expires_in = expiration)
    	return s.dumps({'id': self.username })

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
    	user_id = data['username']
    	return user_id




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
    	user_id = data['username']
    	return user_id


Base.metadata.create_all(engine)