from flask import g,jsonify,abort
from flask_restful import Resource,reqparse
from sqlalchemy.orm import relationship, sessionmaker,scoped_session
from sqlalchemy import create_engine
from flask_httpauth import HTTPBasicAuth
from SECURITY.model import User,base



auth= HTTPBasicAuth()

engine = create_engine('sqlite:///usersWithTokens.db' , connect_args={'check_same_thread':False})

#base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@auth.verify_password
def verify_password(username_or_token, password):
    decorators = [auth.verify_password]
    #return True
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(username = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


class get_auth_token(Resource):
    decorators = [auth.login_required]
    def get(self):
        token = g.user.generate_auth_token()
        return jsonify({'token': token.decode('ascii')})


class apiusers(Resource):
 def get(self):
      parser = reqparse.RequestParser()
      parser.add_argument('username',required=True,help="username cannot be blank!")
      args = parser.parse_args()
      username = args['username']
      user = session.query(User).filter_by(username=username).one()
      if not user:
         return jsonify({'ERROR': 'username does not exist'})
      return jsonify({'username': user.username})


 def post(self):
  parser = reqparse.RequestParser()
  parser.add_argument('username',required=True,help="username cannot be blank!")
  parser.add_argument('password',required=True,help="username cannot be blank!")
  args = parser.parse_args()
  username = args['username']
  password = args['password']
  if username is None or password is None:
        print ("missing arguments")
        abort(400)
  if session.query(User).filter_by(username = username).first() is not None:
        print( "existing user")
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'})# , 200#, {'Location': url_for('get_user', id = user.id, _external = True)}

  user = User(username = username)
  user.hash_password(password)
  session.add(user)
  session.commit()
  session.delete()
  return jsonify(usercreated={ 'username': user.username }) # , 201#, {'Location': url_for('get_user', id = user.id, _external = True)}


#engine = create_engine('sqlite:///usersWithTokens.db')
#Base.metadata.create_all(engine)

# class get_user(Resource):
#     def get(self):
#       parser = reqparse.RequestParser()
#       parser.add_argument('username',required=True,help="username cannot be blank!")
#       args = parser.parse_args()
#       username = args['username']
#       user = session.query(User).filter_by(username=username).one()
#       if not user:
#         abort(400)
#       return jsonify({'username': user.username})

