from flask import Flask,send_from_directory
from flask_restful import Resource, Api
from EXPANDABLE import Expandable,Expandable_New
from EEPROM import  Eeprom
from KPI import Kpi
from SFDC import sfdc
from UTIL import ixiapidoc
from SECURITY import  mysecurity,model
from OMNIFY import omnify
from AD import ad
from ALM import alm
from flask_httpauth import HTTPBasicAuth
app = Flask(__name__,static_url_path='')
auth= HTTPBasicAuth()
import types


@app.route('/')
@app.route('/api')
#@auth.login_required
def hello_world():
    return app.send_static_file('index.html')
api = Api(app)

def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)

#api.add_resource(ixiapidoc.Showhelp, '/api')
api.add_resource(Expandable.delay, '/api/exp')
api.add_resource(Expandable.users, '/api/exp/users')
api.add_resource(Expandable_New.jobs, '/api/exp/jobs')
#api.add_resource(Expandable.parts, '/api/exp/parts')
#api.add_resource(Expandable.users, '/api/exp/users')

api.add_resource(Eeprom.parts, '/api/epr/parts')
api.add_resource(Eeprom.logininfo, '/api/epr/logininfo')
api.add_resource(Eeprom.jobinfo, '/api/epr/jobinfo')

api.add_resource(Eeprom.rfid, '/api/rfid/jobinfo')


api.add_resource(Kpi.kpis, '/api/kpi/all')
api.add_resource(Kpi.kpi, '/api/kpi/<kpicode>')



api.add_resource(sfdc.Opurtinity, '/api/sfdc/opportunity')
api.add_resource(sfdc.Pricebook, '/api/sfdc/pricebook')
api.add_resource(sfdc.Product, '/api/sfdc/product')
api.add_resource(sfdc.User, '/api/sfdc/user')
api.add_resource(sfdc.Account, '/api/sfdc/account')
api.add_resource(sfdc.Case, '/api/sfdc/case')
api.add_resource(sfdc.SOFOD, '/api/sfdc/sofod')


api.add_resource(sfdc.Report, '/api/sfdc/report')

api.add_resource(sfdc.SOLUTION, '/api/sfdc/solution')


api.add_resource(alm.UpdateALM, '/api/alm/sfdefect')
api.add_resource(alm.Defectslist, '/api/alm/defect')
api.add_resource(alm.Htmltest, '/api/alm/html')



api.add_resource(sfdc.RunReport_Forecast_PIP, '/api/sfanalytic/forecast')
api.add_resource(sfdc.Run_Exp_SF4_Cleanup, '/api/sfanalytic/expsfdc')
api.add_resource(sfdc.SFDC_EXP_DESCREPENCY, '/api/sfanalytic/descrepency')


api.add_resource(ad.Authenticate, '/api/ad/authenticate')


api.add_resource(omnify.PartMismatch, '/api/omnify/partmismatch')



api.add_resource(mysecurity.apiusers, '/api/sec/user')
#api.add_resource(mysecurity.new_user, '/api/sec/newuser')
api.add_resource(mysecurity.get_auth_token, '/api/sec/token')



if __name__ == '__main__':
    app.run(debug=True,port=8090)
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'