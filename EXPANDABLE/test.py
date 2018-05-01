
from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESI_SANDBOX')
jobss_as_dict=[]
connection = engine.raw_connection()
cursor = connection.cursor()
cursor.execute("select JOB_ID,JOB_STATUS,JOB_TYPE,DATE_LAST_UPDT  from JCFJM")


mylist=[]
for row in cursor:

     mylist.append(row)
     val = mylist[0]
     print(val[1])
     mylist.pop()
     # with engine.connect() as con:
     #     rs=con.execute("select JOB_ID,JOB_STATUS,JOB_TYPE,DATE_LAST_UPDT  from JCFJM ")
     #     for row in rs:
     #         job_as_dict = {
     #               'JOB_ID' : row(0) }