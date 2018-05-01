from __future__ import division
import os
# with open('C:\Python34\NEWS.txt','r') as f:
#     line=f.readlines()
#     for s in line:
#         print(s)
# data = [115, 140, 175]
# max=max(data)
# print(max)
#from __future__ import division

# def featureScaling(arr):
#     scaled = []
#     min1 = min(arr)
#     max1 = max(arr)
#     for i in arr:
#         print(i)
#         newval = (i-min1) / (max1 - min1)
#         scaled.append(newval)
#
#     return scaled
#
#
# # tests of your feature scaler--line below is input data
# data = [115, 140, 175]
# print featureScaling(data)
#from os import getenv
import pymssql
import psycopg2
import sys
##from pymysql.cursors import DictCursor
conn_string = "host='192.168.3.146' dbname='ESIDB' user='postgres' password='123456'"
psqlconn = psycopg2.connect(conn_string)
# psqlsqltext = """
#
#
# SELECT  * from ALFTD LIMIT 10;
#
# """
psqlcur = psqlconn.cursor()
psqlcur.execute(
    """ INSERT INTO alftd(recnum, program_id, table_name, operator_id, first_name, last_name, initial, machine, trigger_type, key1, key2, key3, key4, key5, key6, maint_log, time_last_updt, date_last_updt, delete_flag) values (21825067,'.Net SqlClient Data Provider','ICFPM','UNKNOWN','None','None','','IXI-ERP','UPDATE                   ','P043102','','','','','','DWG_REV: BEFORE: F; AFTER: G\r\nECN_EFF_DATE: BEFORE: 01/29/2018; AFTER: 02/01/2018\r\nICFPM_USER_11: BEFORE: ECO-002052; AFTER: ECO-002064\r\nTIME_LAST_UPDT: BEFORE: 10:01; AFTER: 16:42\r\nDATE_LAST_UPDT: BEFORE: 01/29/2018; AFTER: 02/01/2018','16:42','2018-02-01 00:00:00','N')
""")
psqlconn.commit()
# for row in psqlcur:
#     #val=dict(row)
#     #values=row(0).split(',')
#     #print(row['CHANGE_TYPE'])
#     #print(row['RECNUM'])
#     #print(row['FIRST_NAME'])
#     #print(row['LAST_NAME'])
#     print(row)



conn = pymssql.connect(host='192.168.3.40', user='sysdba', password='e$1s_s', database='JOANNATRAINING')
s = """

SELECT   * from ALFTD with (NOLOCK) where DATE_LAST_UPDT>'2018-02-28 00:00:00.000' and RECNUM>22504376    order by RECNUM,DATE_LAST_UPDT 


"""
cur = conn.cursor(as_dict=True)
cur.execute(s)
i=0
for row in cur:
    i+=1
    errsql=[]
    RECNUM=row['RECNUM']
    PROGRAM_ID=row['PROGRAM_ID'].strip()
    TABLE_NAME=row['TABLE_NAME'].strip()
    OPERATOR_ID=row['OPERATOR_ID'].strip()
    FIRST_NAME=row['FIRST_NAME']
    LAST_NAME=row['LAST_NAME']
    #INITIAL=row['INITIAL']
    INITIAL = '' if row['INITIAL'] == None else row['INITIAL']
    MACHINEprint=row['MACHINE'].strip()
    CHANGE_TYPE= '' if  row['CHANGE_TYPE']== None  else row['CHANGE_TYPE']
    #count = 0 if row['CHANGE_TYPE'] != None else CHANGE_TYPE = ''
    KEY1= row['KEY1'].strip()
    KEY2=row['KEY2'].strip()
    KEY3=row['KEY3'].strip()
    KEY4=row['KEY4'].strip()
    KEY5=row['KEY5'].strip()
    KEY6 = row['KEY5'].strip()
    MAINT_LOG=row['MAINT_LOG'].strip()
    TIME_LAST_UPDT=row['TIME_LAST_UPDT']
    DATE_LAST_UPDT=row['DATE_LAST_UPDT']
    DELETE_FLAG=row['DELETE_FLAG'].strip()

    psqlsqltext = 'INSERT INTO alftd(recnum, program_id, table_name, operator_id, first_name, last_name, ' \
                  'initial, machine, trigger_type, key1, key2, key3, key4, key5, key6, maint_log, time_last_updt,' \
                  ' date_last_updt, delete_flag) ' \
                  'values ('+ str(RECNUM)+','+ repr(str(PROGRAM_ID))+','+ repr(str(TABLE_NAME))+','+ repr(str(OPERATOR_ID))+','+ repr(str(FIRST_NAME))+','+ repr(str(LAST_NAME))+',' \
                  ''+ repr(str(INITIAL))+','+ repr(str(MACHINEprint))+','+ repr(str(CHANGE_TYPE))+','+ repr(str(KEY1))+','+ repr(str(KEY2))+','+ repr(str(KEY3))+','+ repr(str(KEY4))+','+ repr(str(KEY5))+','+ repr(str(KEY6))+','+ repr(str(MAINT_LOG))+','+ repr(str(TIME_LAST_UPDT))+','+ repr(str(DATE_LAST_UPDT))+','+ repr(str(DELETE_FLAG))+')'

    #psqlcur = psqlconn.cursor()
    #psqlcur.execute(s)
    print(i)
    #print(psqlsqltext)
    try:

        psqlcur.execute(psqlsqltext)
        psqlconn.commit()
    except Exception as e:
        errsql.append(psqlsqltext)
        print(psqlsqltext)

