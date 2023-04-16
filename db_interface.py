from face_db_interface import FaceDBInterface
from sql_db_interface import SQLDBInterface
import os
class DBInterace(object):

    def __init__(self,db_name='',k=5) -> None:
        self.k = k
        self.face_db = FaceDBInterface(face_directory='face',db_name=db_name,k=self.k)
        self.sql_db = SQLDBInterface(db_name=db_name)
        print('[+] Everything loaded')
    
    def enroll(self,name,address,city,state,zip,filename):
        
        id = self.face_db.enroll_face(file_name=filename)
        id = str(id)
        self.sql_db.insert(id,name,address,city,state,zip,filename)
        print('[+] Data Inserted ')
        return id

    def reterive(self,filename):
        data_json = {}
        try:
            percentage,matches=self.face_db.reterive_face(file_name=filename)
            for i in range(self.k):
                data_json[i]={}
                percnt = percentage[0][i]
                id = matches[0][i]
                data = self.sql_db.get_data(id=id)
                data_json[i]['name']=data[1]
                data_json[i]['address']=data[2]
                data_json[i]['city']=data[3]
                data_json[i]['state']=data[4]
                data_json[i]['zip']=data[5]
                data_json[i]['filename']=os.path.basename(data[6])
                data_json[i]['percentage']=float(percnt)
            data_json['status']=True
        except Exception as e:
            data_json['status']=False
            data_json['error']= str(e)
        return data_json
        
    # print(data)
