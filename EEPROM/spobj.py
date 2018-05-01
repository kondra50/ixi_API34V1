from sqlalchemy import create_engine,bindparam
from sqlalchemy.orm import sessionmaker
engine = create_engine('mssql+pymssql://sysdba:e$1s_s@192.168.3.40:1433/ESIDB')
class Spjobsinfo():
     def __int__(self,PART_ID,PART_DESC,MFG_DATE,SHELF_LIFE,CTYPE,HasAccess,NOU,PPJ,Part_Programmed,ERRCODE):
         self.PART_ID= PART_ID,
         self.PART_DESC= str(PART_DESC).strip(),
         self.MFG_DATE= MFG_DATE,
         self.SHELF_LIFE= SHELF_LIFE,
         self.CTYPE= CTYPE,
         self.HasAccess= HasAccess,
         self.NOU= NOU,
         self.PPJ= PPJ,
         self.Part_Programmed= Part_Programmed,
         self.ERRCODE= ERRCODE,

     def Load(self,JobId,Username):
         try:
          connection = engine.raw_connection()
          cursor = connection.cursor()
          cursor.callproc('[Admin_EPROM_GETJOBINFO_API]',[JobId,Username])
          #print(JobId)
          #cursor.callproc("select * from LDFEM")
          #self.__int__(self,cursor(0)[0],cursor(0)[1],cursor(0)[2],cursor(0)[3],cursor(0)[4],cursor(0)[5],cursor(0)[6],cursor(0)[7],cursor(0)[8],cursor(0)[9])
          for row in cursor:
               mylist=[]
               mylist.append(row)
               val = mylist[0]
               self.__int__(self,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9])

         except Exception as e:
            print(e)
         finally:
          cursor.close()
          connection.commit()
          connection.close()
          return self
     def Update(jobid,machin_name,cartridge_id,exp_date,username):
         val=[]
         mylist=[]
         try:
          connection = engine.raw_connection()
          cursor = connection.cursor()
          cursor.callproc('[Admin_EPROM_UPDATE_EXPDATE_API]',[jobid,machin_name,cartridge_id,exp_date,username])
          for row in cursor:
               mylist.append(row)
               val = mylist[0]
               return {
                  'PP_UPDATED':val[0],
                  'PART_PROGRAMMED':val[1],
                  'EXPDATE_UPDATED':val[2]
               }
         except Exception as e:
            return {
                  'ERROR': str(e)
               }
         finally:
          cursor.close()
          connection.commit()
          connection.close()

     def UpdateRFID(jobid,machin_name,cartridge_id,serialnumber,username):
         val=[]
         mylist=[]
         try:
          connection = engine.raw_connection()
          cursor = connection.cursor()
          cursor.callproc('[Admin_EPROM_UPDATE_EXPDATE_RFID_API]',[jobid,serialnumber,machin_name,cartridge_id,username])
          for row in cursor:
               mylist.append(row)
               val = mylist[0]
               return {
                  'SN_UPDATED':val[0],
                  'PP_UPDATED':val[1],
                  'PART_PROGRAMMED':val[2]
               }
         except  Exception as e:
            return {
                  'ERROR': str(e)
               }
         finally:
          cursor.close()
          connection.commit()
          connection.close()

     def serialize(Self):
        print(Self.ERRCODE[0])
        return  {
                'PART_ID': Self.PART_ID[0],
                'PART_DESC': Self.PART_DESC[0],
                'MFG_DATE':Self.MFG_DATE[0],
                'SHELF_LIFE': Self.SHELF_LIFE[0],
                'CTYPE' : Self.CTYPE[0],
                'HasAccess':Self.HasAccess[0],
                'NOU' : Self.NOU[0],
                'PPJ' : Self.PPJ[0],
                'Part_Programmed': Self.Part_Programmed[0],
                'ERRCODE': Self.ERRCODE[0]
                }
class Splogininfo():
    def __int__(self,USERNAME,GROUP_NAME,ACCESS):
         self.USERNAME= USERNAME,
         self.GROUP_NAME= GROUP_NAME,
         self.ACCESS= ACCESS,

    def Load(self,ldapuser):
         #try:
          #myobjlist=[]
          connection = engine.raw_connection()
          cursor = connection.cursor()
          cursor.callproc('[Admin_EPROM_LOGININFO_API]',[ldapuser])
          for row in cursor:
               mylist=[]
               mylist.append(row)
               val = mylist[0]
               self.__int__(self,val[0],val[1],val[2])
               #myobjlist.append(self)

         #except:
          print(self.GROUP_NAME[0])
         #finally:
          cursor.close()
          connection.commit()
          connection.close()
          return self

    def serialize(Self):
        return {
       	    'USERNAME':Self.USERNAME[0],
            'GROUP_NAME': Self.GROUP_NAME[0],
            'ACCESS': Self.ACCESS[0],
       }

class SpPart(object):
 def __int__(self,PART_ID,ICFPM_USER_16):
        self.PART_ID= PART_ID,
        self.ICFPM_USER_16= ICFPM_USER_16

 # def __new__(object,PART_ID,ICFPM_USER_16):
 #        PART_ID= PART_ID,
 #        ICFPM_USER_16= ICFPM_USER_16
 @property
 def serialize(Self):
    return {
    'PART_ID':Self.PART_ID,
    'ICFPM_USER_16': Self.ICFPM_USER_16
       }


def LoadPart():
         #try:
          parts_as_dict=[]
          connection = engine.raw_connection()
          cursor = connection.cursor()
          cursor.callproc('[Admin_EPROM_PARTSLIST]')
          cursor.callproc('[Admin_EPROM_PARTSLIST]')
          for row in cursor:
               mylist=[]
               mylist.append(row)
               val = mylist[0]
               try:
                    part_as_dict = {
                   'PART_ID' : val[0].strip(),
                   'ICFPM_USER_16' :val[1].strip()
                    }
                    parts_as_dict.append(part_as_dict)
                  # sppart= SpPart(val[0].strip(),val[1].strip())
               except Exception as e:
                   print(e)
               #self.__int__(self,val[0].strip(),val[1].strip())
               #myobjlist.append(sppart)
         #except:
          #print(self.GROUP_NAME[0])
         #finally:
          cursor.close()
          connection.commit()
          connection.close()
          return parts_as_dict


