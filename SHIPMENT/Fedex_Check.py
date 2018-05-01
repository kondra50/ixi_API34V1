import os
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import  MIMEMultipart
path_to_file=os.path.abspath("\\\\ixi-erp\ESI\\SOTSI\\Output from FedEx\\tracking# DO NOT Delete Template.csv")

statinfo = os.stat(path_to_file)
# print(statinfo)
# print(statinfo.st_size)
if (statinfo.st_size>0):

    try:
             msg = MIMEMultipart()
             msg['Subject'] = 'The Fedex Output is not Exported to Expandable '
             msg['From'] = "mehrdadn@integenx.com"
             msg['To'] = "mehrdadn@integenx.com"
             s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
             s.send_message(msg)
             s.quit()
    except Exception as e:
            print(e)





#while (True):

    # statinfo = os.stat(path_to_file)
    # print(statinfo)
    #
    # print(statinfo.st_size)
    # try:
    #      msg = MIMEMultipart()
    #      msg['Subject'] = 'The Fedex Output is not Expoeted to Expandable '
    #      msg['From'] = "mehrdadn@integenx.com"
    #      msg['To'] = "mehrdadn@integenx.com"
    #      s = smtplib.SMTP('IXI-EXCH.microchipbiotech.com')
    #      s.send_message(msg)
    #      s.quit()
    # except Exception as e:
    #     print(e)

    #time.sleep(10)