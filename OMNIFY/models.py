import requests,json
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
Session = scoped_session(sessionmaker(bind=engine))
def PartMitmatch():
      connection = engine.raw_connection()
      cursor = connection.cursor()
      try:
       #list=cursor.callproc('[dbo].[Admin_Omnify_Expandable_Crosscheck3]')
       s = Session()
      #sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
      #result = s.execute("select CATG_CODE,omnify.PartNumber,omnify.[Other(i) Configuration Type] as config  from (SELECT ENTRY.PartNumber, ParamValue.[Other(i) Configuration Type] FROM [IXI-OMNIFY].Omnify45.dbo.ENTRYINNER JOIN [IXI-OMNIFY].Omnify45.dbo.PARAMVALUE ON ENTRY.ID = PARAMVALUE.ITEMIDinner join (select itemid, max(id) as 'currentRev' from [IXI-OMNIFY].Omnify45.dbo.rev WHERE EXPIRED='0' group by itemid) as crev on crev.itemid = PARAMVALUE.ITEMID AND cREV.CURRENTREV = PARAMVALUE.REVIDWHERE ParamValue.[Other(i) Configuration Type] <> 'Not Configured' and ParamValue.[Other(i) Configuration Type] is not null  and ParamValue.[Other(i) Configuration Type] <> ''AND ParamValue.[MRP(c) Part Status] <> 'O-Obsolete') as omnify inner join ICFPM on ICFPM.PART_ID=omnify.PartNumber where CATG_CODE='s'""")
       list=s.execute('[Admin_Omnify_Expandable_Crosscheck3]')
      #list=sf.query("SELECT Approved FROM [Expandable Sales Orders] ")
       prs_as_dict=[]
       for record in  list:
            pr_as_dict = {
                   'CATG_CODE' :  record["CATG_CODE"],
                   'PartNumber' :  record["PartNumber"],
                   'config' :  record["config"],
            }
            prs_as_dict.append(pr_as_dict)
       return prs_as_dict

      except Exception as e:
        return {"ERROR": e}


