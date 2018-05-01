import sqlite3
import os
import time
from simple_salesforce import Salesforce
from tinydb import TinyDB, where,Query
from datetime import datetime, timedelta
db = TinyDB('db.json')
CN = Query()
import salesforce_reporting
# import requests,json
# from flask import jsonify
# from SFDC import  dbmodels
attemts=['RHID','RHIT']

sf = Salesforce(username='customerservice@integenx.com', password='password12345', security_token='3GKZny4jRWgmXNUmvFjzKhggQ')
#db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
#db_path2=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")

for attemt in attemts:

    if attemt=='RHID': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
    if attemt=='RHIT': db_path=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
    #while True:
        #time.sleep(60)
       # print("After 5 sec")
    hastrack= False
    solution=""
    try:
        conn5 = sqlite3.connect(db_path)
        c = conn5.cursor()
        hourago= datetime.now() - timedelta(hours = 1)
        #s='select DefectNum,Summary,Status from DEFECTS inner join DEFECTEVTS on   DEFECTEVTS.ParentID=DEFECTS.idRecord   where dateEvent> '+ str(hourago).rpartition(':')[0]
        s='select DefectNum,Summary,Status,dateModify from DEFECTS  where dateModify >'+ repr(str(hourago).rpartition(':')[0])
        c.execute(s)
        rows=c.fetchall()
        defect_as_dict=[]
        for row in rows:
                DefectNum=row[0]
                Summary=row[1]
                Status=row[3]
                s='select Custvalue from CUSTMVAL where idCustRec=681 and ParentID=' + repr(str(row[0])) + ''
                c.execute(s)
                rows1=c.fetchall()
                casenumber=0
                for row1 in rows1:
                    casenumber=row1[0]
                Synceddict=db.search(CN.casenumber == casenumber)
                s='select Name,dateEvent,DEFECTEVTS.Notes ,OrderNum  from  DEFECTEVTS  inner join EVENTS on   DEFECTEVTS.EvtDefID=EVENTS.idRecord  and ParentID=' + str(row[0]) + ' order by OrderNum'
                c.execute(s)
                tracks_as_dict=[]
                tracktext=""
                tracks=c.fetchall()
                for track in tracks:
                    hastrack= True
                    if (track[0]=="Verified"): solution=track[2]
                    track_as_dict={
                        'Event': track[0],
                        'Date': track[1],
                        'Notes': track[2]
                    }
                    if (hastrack):
                     tracks_as_dict.append(track_as_dict)
                     tracktext=str(tracks_as_dict)



                 #UPDATE WORKFLOW

                list=sf.query("SELECT Id,Defect_Ref__c FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
                dict=list["records"]
                if len(dict)> 0:
                     cid=dict[0]['Id']
                     CurrentDefectNumber=dict[0]['Defect_Ref__c']
                     sf.Case.update(cid,{'Workflow_from_ALM__c': tracktext})
                     if  len(CurrentDefectNumber)== 0:
                        sf.Case.update(cid,{'Defect_Ref__c': DefectNum})





                #UPDATE SOLUTIONS
                if len(Synceddict)==0 and Status == 10:

                    if (str(solution) != ""):

                           list=sf.query("SELECT Id FROM Case WHERE CaseNumber = " + repr(str(casenumber)))
                           dict=list["records"]
                           if len(dict)> 0:
                               print(dict[0]['Id'])
                               cid=dict[0]['Id']
                               mydict = sf.Solution.create({'SolutionNote':solution, 'SolutionName': 'solution - '+ Summary})
                               db.insert({'casenumber': casenumber})
                               print(mydict['id'])
                               sid=mydict['id']
                               solution = sf.Solution.get(mydict['id'])
                               print(mydict['success'])
                               #orderdisc=solution('OrderDict')
                               print(solution['SolutionNumber'])
                               sn=solution['SolutionNumber']

                               mydict = sf.CaseSolution.create({'CaseId': cid ,  'SolutionId':sid})
                               print(mydict)

                #Update case
                #sf.Case.Update

    except  Exception as e:
        print(e)





