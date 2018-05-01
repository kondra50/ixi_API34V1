from waitress import serve
from wsgiref.simple_server import make_server
from IXI_API_app import app
from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('C:\Python34\ixi_API34\keys\privatekey.key')
#context.use_certificate_file('C:\Python34\ixi_API34\keys\certificate.crt')

if __name__ == "__main__":
  serve(app, port=8090 , url_scheme='https')




#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout privatekey.key -out certificate.crt