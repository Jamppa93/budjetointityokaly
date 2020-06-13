from DBMS import DBMS 

class etlManager(): 

    DBMSInst = None 
    cursor = None 
    
    def __init__(self):
     self.DBMSInst = DBMS()
     self.DBMSInst.connectToDatabase()  
     self.cursor = self.DBMSInst.getCursor()
         
    def printObjectType(self):
        print(type(self))
    
    def testDB(self): # WORKS!
        order_num = self.cursor.execute('SELECT COUNT(*)FROM TILAUS')
        order_num = order_num.fetchall()
        for i in order_num:
            order_num = i[0]
        order_num = str(order_num)
        print(order_num)
  

