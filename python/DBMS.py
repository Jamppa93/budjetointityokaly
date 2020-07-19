import pyodbc # https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
import sys
import pathlib # https://docs.python.org/3/library/pathlib.html#module-pathlib


class DBMS(): 
    Conn = None
    #path = pathlib.Path(pathlib.Path(__file__).parents[1].absolute(),'dbFile/budjetointi.db')
    #path = pathlib.Path(pathlib.Path(__file__).parents[1].absolute(),'dbFile/harkka.sql')
    #def __init__(self):
    
    def connectToDatabase(self): # Maybe later make changable conncetion with variables: serverName, databaseName
        #try:
        self.Conn= pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-FBMRT2T;'
                      'Database=budjettiExcel;'
                      'Trusted_Connection=yes;')
        return self.Conn
        
        #except Error as e:
            #print(e)
            #sys.exit(0)  
                    
    def closeConnection(self):
        self.Conn.Close()
                
    def getCursor(self):
        return self.Conn.cursor()
        

