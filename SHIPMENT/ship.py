import csv
import os , datetime
# path_to_file=os.path.abspath("\\\\ixi-erp\ESI\\SOTSI\\Output from FedEx\\tracking# DO NOT Delete Template.csv")
path_to_file=os.path.abspath("\\\\ixi-erp\ESI\\SOTSI\\Output from FedEx\\tracking# DO NOT Delete Template.csv")
from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
print(path_to_file)
import os,time


def readANDinsert():
    connection = engine.raw_connection()
    cursor = connection.cursor()
    f = open(path_to_file)
    csv_f = csv.reader(f)
    freights_as_json = []
    for row in csv_f:

     freight_as_json = {
             'SO_ID': row[1],
             'DATE': row[2],
             'BOL':   row[3],
             'AMOUNT':  row[4],
             'WEIGHT':  row[5],
             'CARTOON':  row[6],
             'ZIPCODE':  row[15],
        }
     # if (row[2]==datetime.date.strftime(datetime.date.today(), "%m/%d/%y")):
     freights_as_json.append(freight_as_json)
        #print(row[2])
        #print(datetime.date.strftime(datetime.date.today(), "%m/%d/%y"))


    for freight in freights_as_json:

         SO_ID=freight['SO_ID']
         DATE=freight['DATE']
         AMOUNT=freight['AMOUNT']
         BOL=freight['BOL']
         WEIGHT=freight['WEIGHT']
         CARTOON=freight['CARTOON']
         ZIPCODE=freight['ZIPCODE']

         #SO_ID=103545
         # print(datetime.date.today())
         print(freight['ZIPCODE'])
         try:

             # sql='select count(*) from [ESIDB].[dbo].[IXI_FEDEX] where SO_ID= ' + repr(str(SO_ID))+' and BILL_OF_LADING=' + str(BOL)+ ' and AMOUNT='+ str(AMOUNT)
             # print(sql)
             # cursor.execute(sql)
             # cnt=cursor.fetchone()[0]
             #if(1>0):
             #if(2>1):
             ACTION_TYPE='FR'
             SHIP_VIA='FedEx Intl Prior'
             sql='INSERT INTO [ESIDB].[dbo].[IXI_FEDEX] ' \
             '([SO_ID] ,[SO_LINE_NO],[ACTION_DATE],[ACTION_TYPE]' \
             ',[AMOUNT]' \
             ',[BILL_OF_LADING],[SHIP_VIA],[WEIGHT],[NUMBER_CARTONS],[DATE_LAST_UPDT]) ' \
             'values(' + repr(str(SO_ID)) + ',999,' + repr(str(DATE)) + ','+repr(str(ACTION_TYPE))+',' + str(AMOUNT) + ',' + repr(str(BOL)) + ','+repr(str(SHIP_VIA))+',' + str(WEIGHT) + ',' + str(CARTOON) + ',' + repr(str(datetime.date.today())) + ')'
             print(sql)
             cursor.execute(sql)
             connection.commit()
         except Exception as e:
             print(e)
         finally:
             print("ok")
    cursor.close()
    connection.commit()
    connection.close()
























 # print(datetime.date.today())
 # d = datetime.datetime.strptime("2013-1-25", '%Y-%m-%d')
 #    while (True):
 #    readANDinsert()
 #    print('Waiting')
 #    time.sleep(10)
def Delete():
    connection = engine.raw_connection()
    cursor = connection.cursor()
    try:
        sql='delete from [ESIDB].[dbo].[IXI_FEDEX]'
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    except Exception as e:
             print(e)


while (True):
    try:

        Delete()
        readANDinsert()
        print('Waiting')
        time.sleep(10)
    except Exception as e:
             print(e)

# with open("\\\\ixi-erp\ESI\\SOTSI\\Output from FedEx\\tracking# DO NOT Delete Template.csv", 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# workbook = xlrd.open_workbook(path_to_file)
#
# sheet=workbook.sheet_by_index(0)
# freights_as_json=[]

# for row_index in range(1, sheet.nrows):
#     print (sheet.cell(row_index, 2).value)
#     freight_as_json = {
#          'SO_ID': sheet.cell(row_index, 2).value,
#          'AMOUNT': sheet.cell(row_index, 5).value,
#          'BOL': sheet.cell(row_index, 4).value,
#          'WEIGHT': sheet.cell(row_index, 6).value,
#          'CARTOON': sheet.cell(row_index, 7).value,
#          'ZIPCODE': sheet.cell(row_index, 16).value,
#     }
#
#     freights_as_json.append(freight_as_json)

# workbook1 = self.Workbook(self.dataDir + 'Book1.xls')
# worksheet = workbook.sheet_by_index(0)
# worksheet.get_rows().delete()

# os.rename('C:\Python34\ixi_API34\SHIPMENT\\tracking.xls','C:\Python34\ixi_API34\SHIPMENT\\tracking_proceed.xls')

# C:\Users\mehrdad.nafisi\Desktop\RHID.xls
# from openpyxl import load_workbook
# wb = load_workbook('Book1.xlsx')
# ws = wb.active
# for row in ws.iter_rows():
#    for cell in row:
#      print cell.value
