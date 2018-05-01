from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, ALL

def CheckAD(username,password):
 username= 'microbio'+ '\\' + username
 s = Server('192.168.3.4', port=389, get_info=ALL)
 #c = Connection(s, authentication=AUTH_SIMPLE, user='microbio\mehrdad.nafisi', password='INTgsm7!7', check_names=True, lazy=False, client_strategy=STRATEGY_SYNC, raise_exceptions=True)
 c = Connection(s, authentication=AUTH_SIMPLE, user=username, password=password, check_names=True, lazy=False, client_strategy=STRATEGY_SYNC, raise_exceptions=True)
 try:
  c.open()
  c.bind()
  return {'Authenticate':"Successful"}
 except Exception as e:
  return {'Authenticate':"InvalidCredentials"}
  print(e)