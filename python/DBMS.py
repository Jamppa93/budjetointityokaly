import sqlite3
import sys
import pathlib # https://docs.python.org/3/library/pathlib.html#module-pathlib


class DBMS(): 
    Connections = None
    path = pathlib.Path(pathlib.Path(__file__).parents[1].absolute(),'dbFile/harkka.sql')
    #def __init__(self):

    
    def connectToDatabase(self):
        try:
            self.Connections = sqlite3.connect(self.path)
            return 
        except Error as e:
            print(e)
            sys.exit(0)  
                    
    def closeConnections(self):
        self.Connections.close()
                
    def getCursor(self):
        return self.Connections.cursor()
        

