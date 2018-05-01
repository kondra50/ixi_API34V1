import sqlite3
import os,time
from flask import  abort
# notfound = 404
# Forbiden = 403
# ok = 200
db_path2=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\ttproj.db")
db_pathRH=os.path.abspath("\\\\IXI-APPSVR02\\RapidHIT Sustaining\\ttproj.db")
db_lock=os.path.abspath("\\\\IXI-APPSVR02\\RHID Sustaining Production\\project.lock")
def Update(RecortType,caseNumber,SerialNumber,CustGUI,CCSN,Craetedby,OwnerId,Subject,Desc,Module,PrimeCart,CartridgeLot,product,runlogname,fversion,runonpcart,customer):
    if (RecortType=="technical"):
        try:
            db_path = os.path.abspath("\\\\ixi-datasvr.microchipbiotech.com\\Public\\Mehrdad Nafisi\\ttproj.db")
            userid=getUserID(Craetedby, db_path)
            max1=getlastID(db_path)
            moduleid=getModulID(Module, db_path)
            conn = sqlite3.connect(db_path)
            c = conn.cursor()

            st='insert into DEFECTS(ProjectID,idRecord,idCreateBy,dateCreate,Summary,Status,InitStatus,idType,idCompon) VALUES (1,'+ str(max1) + ', '+ str(userid) + ' ,CURRENT_TIMESTAMP,'+ repr(str(Subject)) + ',1,1,6,'+ str(moduleid) + ')'
            print(st)
            c.execute(st)
            conn.commit()
            conn.close()
            return {'Successfull':"The database 1 has been updated correctly!"}
        except Exception as e:
            return e

    elif (RecortType=="RHID"):
        try:
            #\\IXI-APPSVR02\RHID Sustaining Sandbox  C:\Users\mehrdad.nafisi\Desktop\examples
            if (os.path.isfile(db_lock)):
                return  {"ERROR":"The Project Is locked. Contact the Admin to unlock it!"}
            db_path = db_path2
            print(db_path)
            ##########################################

            if (isDuplicated(RecortType,caseNumber) == True):
                return {"Error":"This Case number is already Exist in ALM!"}


            ##########################################
            userid=getUserID(Craetedby,db_path)
            print(userid)
            res=getlastID(db_path)
            maxid=res['id']
            maxDefNumber=res['RecNum']
            print(maxid)
            moduleid=getModulID(Module,db_path)
            print(moduleid)
            conn = sqlite3.connect(db_path , isolation_level="EXCLUSIVE")
            c = conn.cursor()
           # c.execute('PRAGMA journal_mode=wal')
            st='insert into DEFECTS(ProjectID,idRecord,idCreateBy,dateCreate,Summary,Status,InitStatus,idType,idCompon,DefectNum,IdSeverity,IdEnterBy,dateEnter,idProduct)' \
               ' VALUES (1,'+ str(maxid) + ', '+ str(userid) + ' ,CURRENT_TIMESTAMP,'+ repr(str(Subject)) + ',1,1,7,67,'+ str(maxDefNumber) + ',5,'+ str(userid) + ' ,CURRENT_TIMESTAMP,36)'
            #st='insert into DEFECTS(ProjectID,idRecord,idCreateBy) VALUES (1,'+ str(max1) + ', '+ str(userid)+ ' )'
            c.execute(st)

            #CaseNumber
            Custval=getCustomeValID(db_path)
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 681 ,0,'+ repr(str(caseNumber)) + ')'
            c.execute(st)

            #IssueType
            # Custval=Custval+1
            # st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 1069 ,0,6)'
            # c.execute(st)

            #Source
            # Custval=Custval+1
            # st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 679 ,0,198)'
            # c.execute(st)

            #Severity
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 679 ,0,84)'
            c.execute(st)

             #Module
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 666 ,0,'+ str(moduleid) + ')'
            c.execute(st)

            #Instrument
            Custval=Custval+1
            Instrumentid=getInstrumentID(SerialNumber,db_path)
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 680 ,0,'+ str(Instrumentid) + ')'
            c.execute(st)


            #CartridgeLot
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 664 ,0,'+ repr(str(CartridgeLot)) + ')'
            c.execute(st)





            #PrimeCart
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 678 ,0,'+ repr(str(PrimeCart)) + ')'
            c.execute(st)



            #CCSN
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 670 ,0,'+ repr(str(CCSN)) + ')'
            c.execute(st)




           # fversionNumber=getFVERSIONID(fversion,db_path)

         #############################################
            val='N'

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 665 ,0,0)'
            c.execute(st)
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 667 ,0,'+ repr(str(runlogname)) + ')'
            c.execute(st)
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 685 ,0,'+ repr(str(fversion)) + ')'
            c.execute(st)
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 669 ,0,'+ repr(str(val)) + ')'
            c.execute(st)
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 670 ,0,0)'
            c.execute(st)
            #c.execute(st)
            if (not runonpcart.isdigit()): runonpcart=0
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 671 ,0,'+ str(runonpcart) + ')'
            c.execute(st)
            #c.execute(st)
            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 672 ,0,'+ repr(str(CustGUI)) + ')'
            c.execute(st)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 673 ,0,'+ repr(str(val)) + ')'
            c.execute(st)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 674 ,0,'+ repr(str(val)) + ')'
            c.execute(st)


            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 675 ,0,'+ repr(str(val)) + ')'
            c.execute(st)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 676 ,0,'+ repr(str(val)) + ')'
            c.execute(st)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 682 ,0,0)'
            c.execute(st)

         #############################################


            #CUSTGUIID=getCUSTGUI(CustGUI,db_path)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 686 ,0,'+ repr(str(CustGUI)) + ')'
            c.execute(st)

            Custval=Custval+1
            st='insert into CUSTMVAL(ProjectID,idRecord,ParentID,idCustRec,HasError,CustValue) VALUES (1,'+ str(Custval) + ', '+ str(maxid) + ' , 684 ,0,'+ repr(str(customer)) + ')'
            c.execute(st)






            ReportByID=getReportByID(db_path)
            st='insert into REPORTBY(ProjectID,idRecord,idFoundBy,dateFound,OrderNum,Descrptn,TstConType,idConfig,idDefRec) VALUES (1,'+ str(ReportByID) + ',  ' + str(userid) + ' , CURRENT_TIMESTAMP ,1,'+ repr(str(Desc)) + ',1,4294967293,'+ str(maxid) + ')'
            c.execute(st)




            logid=getLogID(db_path)
            note='Issue Was Added'
            st='insert into DEFLOG(ProjectID,idRecord,idUser,datelog,Notes,parentID) VALUES (1,'+ str(logid) + ',  ' + str(userid) + ' , CURRENT_TIMESTAMP ,'+ repr(str(note)) + ','+ str(maxid) + ')'
            c.execute(st)



            conn.commit()


            checkpoint(db_path)
            #-----------------------------------------------------------------
            #-----------------------------------------------------------------
            # db = sqlite3.connect(db_path)
            # cursor = db.cursor()
            # cursor.execute("PRAGMA wal_autocheckpoint = 0")
            # cursor.execute("PRAGMA wal_checkpoint(PASSIVE)")
            # # while True:
            # #     time.sleep(10)
            #
            # #-----------------------------------------------------------------
            #
            #
            # c.execute('PRAGMA journal_mode=wal')
            # print("done")
            conn.close()
            return {'Successfull':"The defect has been sent to RHID database!"
                    ,'CreartedBy': Craetedby
                    ,'Subject': Subject
                    ,'Case Number': caseNumber
                    ,'ALM Defect Number': maxDefNumber

                    }
        except Exception as e:
            return e
    else:
        abort(404)

       # return {
       #          "error": 403,
       #          "Description": "RecordType is invalid"
       #              }, invalid

def getUserID(Fullname,db_path):
    try:
     id=0
     conn1 = sqlite3.connect(db_path)
     c = conn1.cursor()
     Fullname=Fullname.replace(" ", "")
     s='select max(idRecord) from USERS where lower((FirstName||LastName))=' + repr(Fullname.lower()) + ''
     c.execute(s)
     r=c.fetchall()
     val = r[0]
     conn1.commit()
     if  val[0] is not None: id=val[0]
     return id
    except Exception as e:
        return (0)

def getlastID(db_path):

     try:
        conn2 = sqlite3.connect(db_path)
        c = conn2.cursor()
        s='select max(idRecord),max(DefectNum) from DEFECTS'
        c.execute(s)
        r=c.fetchall()
        if (r[0][0] is None ):
         val1 = 1
         val2 = 1
        else:
         val1 = r[0][0]+1
         val2 = r[0][1]+1
        #print(val[0][0])
        conn2.commit()
        conn2.close()
        return {'id': val1 , 'RecNum' : val2}
     except  Exception as e:
        return (0)

def getModulID(Modulename,db_path):

    try:
     id=0
     conn3 = sqlite3.connect(db_path)
     c = conn3.cursor()
    #s='select max(idRecord) from FLDCOMP where Descriptor=' + repr(Modulename) + ''
     s='select max(idRecord) from  FLDCUSTM where idPUList=17 and  lower(Descriptor)=' + repr(Modulename.lower()) + ''
     c.execute(s)
     r=c.fetchall()
     val = r[0]
     conn3.commit()
     conn3.close()
     if  val[0] is not None: id=val[0]
     return id

    except Exception as e:

        return (e)


def getFVERSIONID(Fversion,db_path):

    try:
     id=0
     conn3 = sqlite3.connect(db_path)
     c = conn3.cursor()
    #s='select max(idRecord) from FLDCOMP where Descriptor=' + repr(Modulename) + ''
     s='select max(idRecord) from  FLDCUSTM where idPUList=18 and  lower(Descriptor)=' + repr(Fversion.lower()) + ''
     c.execute(s)
     r=c.fetchall()
     val = r[0]
     conn3.commit()
     conn3.close()
     if  val[0] is not None: id=val[0]
     return id

    except Exception as e:

        return (e)

def getCUSTGUI(CustGUI,db_path):

    try:
     id=0
     conn3 = sqlite3.connect(db_path)
     c = conn3.cursor()
    #s='select max(idRecord) from FLDCOMP where Descriptor=' + repr(Modulename) + ''
     s='select max(idRecord) from  FLDCUSTM where idPUList=21 and  lower(Descriptor)=' + repr(CustGUI.lower()) + ''
     c.execute(s)
     r=c.fetchall()
     val = r[0]
     conn3.commit()
     conn3.close()
     if  val[0] is not None: id=val[0]
     return id

    except Exception as e:

        return (e)

def getInstrumentID(SerialNumber,db_path):

    try:
     id=0
     conn3 = sqlite3.connect(db_path)
     c = conn3.cursor()
     s='select max(idRecord) from FLDCUSTM where idPUList=20 and lower(Descriptor)=' + repr(SerialNumber.lower()) + ''
     c.execute(s)
     r=c.fetchall()
     val = r[0]
     conn3.commit()
     conn3.close()
     if  val[0] is not None: id=val[0]
     return id

    except Exception as e:

        return (e)

def getCustomeValID(db_path):

     try:
        conn2 = sqlite3.connect(db_path)
        c = conn2.cursor()
        s='select max(idRecord) from CUSTMVAL'
        c.execute(s)
        r=c.fetchall()
        val1 = r[0][0]+1
        conn2.commit()
        conn2.close()
        return val1
     except  Exception as e:
        return (0)

def getReportByID(db_path):

     try:
        conn2 = sqlite3.connect(db_path)
        c = conn2.cursor()
        s='select max(idRecord) from REPORTBY'
        c.execute(s)
        r=c.fetchall()
        val1 = r[0][0]+1
        conn2.commit()
        conn2.close()
        return val1
     except  Exception as e:
        return (0)



def getLogID(db_path):

     try:
        conn2 = sqlite3.connect(db_path)
        c = conn2.cursor()
        s='select max(idRecord) from DEFLOG'
        c.execute(s)
        r=c.fetchall()
        val1 = r[0][0]+1
        conn2.commit()
        conn2.close()
        return val1
     except  Exception as e:
        return (0)



def List(RecortType,CasenNmber):
    defects_as_dict=[]
    if (RecortType=="RH_Technical"):
        try:
            db_path = db_pathRH
            conn = sqlite3.connect(db_path , isolation_level=None)
            c = conn.cursor()
            st='select max(ParentID) from CUSTMVAL where idCustRec=1072 and Custvalue=' + repr(str(CasenNmber)) + ''
            #st='select ProjectID,idRecord,idCreateBy,dateCreate,Summary,Status,InitStatus,DefectNum from DEFECTS order by DefectNum desc'
            c.execute(st)
            r=c.fetchall()
            ParentID = r[0][0]
            conn.close()
            if (ParentID is None):
              return {'Info':'This case number doesnt exist in ALM'}
            elif (ParentID is not None):
             res=GetDefectDetails(db_path, ParentID)
             return res
        except Exception as e:

             return e
    elif (RecortType=="RHID_Technical"):
       try:
            db_path = db_path2
            conn = sqlite3.connect(db_path , isolation_level=None)
            c = conn.cursor()
            st='select max(ParentID) from CUSTMVAL where idCustRec=681 and Custvalue=' + repr(str(CasenNmber)) + ''
            #st='select ProjectID,idRecord,idCreateBy,dateCreate,Summary,Status,InitStatus,DefectNum from DEFECTS order by DefectNum desc'
            c.execute(st)
            r=c.fetchall()
            ParentID = r[0][0]
            conn.close()
            if (ParentID is None):
              return {'Info':'This case number doesnt exist in ALM'}
            elif (ParentID is not None):
             res=GetDefectDetails(db_path,ParentID)
             return res
       except Exception as e:

             return e
    else:
        abort(404)


def isDuplicated(RecortType,CasenNmber):
    defects_as_dict=[]
    if (RecortType=="technical"):
        try:
            print("ok")
        except Exception as e:
             return e
    elif (RecortType=="RHID"):
       try:
            db_path = db_path2
            conn = sqlite3.connect(db_path , isolation_level=None)
            c = conn.cursor()
            st='select max(ParentID) from CUSTMVAL where idCustRec=681 and Custvalue=' + repr(str(CasenNmber)) + ''
            #st='select ProjectID,idRecord,idCreateBy,dateCreate,Summary,Status,InitStatus,DefectNum from DEFECTS order by DefectNum desc'
            c.execute(st)
            r=c.fetchall()
            ParentID = r[0][0]
            conn.close()
            if (ParentID is None):
              return False
            elif (ParentID is not None):
             return True
       except Exception as e:

             return e
    else:
        abort(404)






def GetDefectDetails(db_path,idRecord):
    output_as_dict=[]
    try:
        conn5 = sqlite3.connect(db_path)
        c = conn5.cursor()
        s='select DefectNum,STATES.Name from DEFECTS inner join STATES on STATES.idRecord=DEFECTS.Status where DEFECTS.idRecord=' + str(idRecord) + ''
        c.execute(s)
        rows=c.fetchall()
        defect_as_dict=[]
        for row in rows:
                defect_as_dict={
                        'DefectNumber': row[0],
                        'Status': row[1]
                }
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        output_as_dict.append(defect_as_dict)
        s='select Name,dateEvent,LastName,Firstname,DEFECTEVTS.Notes ,OrderNum  from  DEFECTEVTS  inner join EVENTS on   DEFECTEVTS.EvtDefID=EVENTS.idRecord   inner join USERS  on USERS.idRecord=DEFECTEVTS.idUser  where  ParentID=' + str(idRecord) + ' order by OrderNum'
        c.execute(s)
        rows=c.fetchall()
        tracks_as_dict=[]
        for row in rows:
                track_as_dict={
                        'Event': row[0],
                        'Date': row[1],
                        'Name': row[2]+''+row[3],
                        'Notes': row[4],

                }
                tracks_as_dict.append(track_as_dict)
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        conn5.commit()
        conn5.close()
        output_as_dict.append(tracks_as_dict)
        #full_as_disct = defect_as_dict + track_as_dict
        return output_as_dict
    except  Exception as e:
        return (e)


def checkpoint(db_path):
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    #cursor.execute("PRAGMA wal_autocheckpoint = 0")
    cursor.execute("PRAGMA wal_checkpoint(FULL)")
    # while True:
    #     time.sleep(10)
    #     cursor.execute("PRAGMA wal_checkpoint(PASSIVE)")