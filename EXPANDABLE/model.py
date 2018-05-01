from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
#from sqlalchemy import create_engine
#engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESI_SANDBOX')


def LoadJobs(partid,status):

     jobs_as_dict=[]
     mylist=[]
     try:
         connection = engine.raw_connection()
         cursor = connection.cursor()
         sql="select JOB_ID,JOB_STATUS,JOB_TYPE,DATE_LAST_UPDT,ltrim(rtrim(PART_ID))  from JCFJM"
         if  str(partid)!='None':
             sql = sql+ " where PART_ID =" + str(repr(partid))

         if  str(status)!='None':
             status=str(status).upper()
             sql = sql+ " and  JOB_STATUS =" + str(repr(status))
             sql.replace("\\", " ")
         cursor.execute(sql)
         for row in cursor:
              mylist.append(row)
              val = mylist[0]
              print(val[1])
              job_as_dict = {
                            'JOB_ID' : val[0],
                            'JOB_STATUS' : val[1],
                            'JOB_TYPE' : val[2],
                            'DATE_LAST_UPDT' : val[3],
                            'PART_ID' : val[4],
                            }
              jobs_as_dict.append(job_as_dict)
              mylist.pop()
         return jobs_as_dict


     except Exception as e:

        return {
                  'ERROR': str(e)
               }
     finally:
         cursor.close()
         connection.commit()
         connection.close()