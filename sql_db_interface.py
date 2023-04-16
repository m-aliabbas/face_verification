import sqlite3
import os

class SQLDBInterface(object):
    def __init__(self,db_name) -> None:
        self.db_name = db_name
        self.conn = None
        if not os.path.isfile(db_name+'.db'):
            self.connect(verbose=True)
            self.make_schema()
            self.disconnect()
            
    def connect(self,verbose=False):
        try:
            self.conn = sqlite3.connect(self.db_name+'.db')
            if verbose:
                print(f'[+] {self.db_name} Database Connected')
        except Exception as e:
            print(f'[-] Connection Error {e}')

    def make_schema(self):
        self.connect()
        
        self.conn.execute('''CREATE TABLE COMPANY
        (ID TEXT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        ADDRESS        TEXT    NOT NULL,
        CITY        TEXT ,
        STATE        TEXT ,
        ZIP          TEXT,
        FILENAME     TEXT    NOT NULL);''')
        print(f'[+] DB Schema Created')

        self.disconnect()
            

    def insert(self,id='',name='',address='',city='',
               state='',zip='',filename=''):
        self.connect()
        params = (id,name,address,city,state,zip,filename)
        self.conn.execute("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?)",params)
        self.conn.commit()
        print('[+] Data inserted ')
        self.disconnect()

    def get_data(self,id):
        self.connect()
        self.rows = self.conn.execute(f"SELECT * FROM COMPANY WHERE ID='{id}'")
        for row in self.rows:
            print(' ')
        self.disconnect()
        try:
            return row
        except:
            return '','','','','','',''
        
    def disconnect(self):
        self.conn.close()


