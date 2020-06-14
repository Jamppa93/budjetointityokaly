from DBMS import DBMS 
import pandas as pd
import numpy as np
import tabula
#import openpyxl 

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
  
    def ListFileToPandasDf(self, tempList):

        tempDF = tempList[0]
        for i in range(len(tempList)-1):
            tempDF = pd.concat([tempDF, tempList[i+1]],ignore_index=True)
        
        cols = [1,2,3,4,5]
        tempDF.drop(tempDF.columns[cols],axis=1,inplace=True)
        tempDF=tempDF.fillna("")
        #######################################################################################################
        
        tempDFExplanation = []
        tempDFDate = []
        
        tempDFExplanationAndTime = tempDF[tempDF.columns[0]]
        for i in range(len(tempDFExplanationAndTime.index)):
            tempString = tempDFExplanationAndTime.iloc[i] 
            if (len(tempString)>11): ####
                
                
                tempDFDate.append(tempString[0:6])
                tempDFExplanation.append(tempString[11:])
            else:
                tempDFDate.append('')
                tempDFExplanation.append('')
        #######################################################################################################
        tempDFMoneyAmount = tempDF[tempDF.columns[1]].astype(str) + tempDF[tempDF.columns[2]].astype(str) 
        
        for i in range(len(tempDFMoneyAmount.index)):
            tempString = tempDFMoneyAmount.iloc[i] 
            if (tempString.find('-') > 0 or tempString.find('+')>0):
                pass
            else:
                tempDFMoneyAmount.iloc[i] = '' 
        #######################################################################################################
        
        tempDF = pd.DataFrame({ 'date': tempDFDate,'transaction':tempDFExplanation, 'amount':tempDFMoneyAmount})
        tempDF = tempDF.drop(tempDF[tempDF.transaction ==''].index)
        tempDF = tempDF.drop(tempDF[tempDF.amount ==''].index)
        
        print(tempDF)

        tempDF.to_excel("output111.xlsx",index=False)
        #print(tempDF)

     