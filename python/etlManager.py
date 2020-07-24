from DBMS import DBMS 
import pandas as pd
import numpy as np
import tabula
import sys
from datetime import datetime

#import openpyxl 

class etlManager(): 

    DBMSInst = None 
    cursor = None 
    conn= None
    
    def __init__(self):
     self.DBMSInst = DBMS()
     self.conn= self.DBMSInst.connectToDatabase()  
     self.cursor = self.DBMSInst.getCursor()
         
    def printObjectType(self):
        print(type(self))
    
    # def getRows(self): # WORKS!
    #     order_num = self.cursor.execute('SELECT COUNT(*)FROM NORDEA_ACCOUNT_STATEMENT')
    #     order_num = order_num.fetchall()
    #     for i in order_num:
    #         order_num = i[0]
    #     order_num = int(order_num)
    #     return order_num
  
    def ListFileToPandasDf(self, tempList):
        
        tempDF = tempList[0]
        for i in range(len(tempList)-1):
            tempDF = pd.concat([tempDF, tempList[i+1]],ignore_index=True)
        
        cols = [1,2,3,4,5]
        tempDF.drop(tempDF.columns[cols],axis=1,inplace=True)
        tempDF=tempDF.fillna("")
        #######################################################################################################
        ## DATE & TRANSACTION COLUMNS 
        tempDFExplanation = []
        tempDFDate = []
        
        tempDFExplanationAndTime = tempDF[tempDF.columns[0]]
        for i in range(len(tempDFExplanationAndTime.index)):
            tempString = tempDFExplanationAndTime.iloc[i] 
            if (len(tempString)>11): ####päiväys?

                tempDFDate.append(tempString[0:6])
                tempDFExplanation.append(tempString[11:])
            else:
                tempDFDate.append('')
                tempDFExplanation.append('')
        #######################################################################################################
        #AMOUNT OF MONEY COLUMN
        tempDFMoneyAmount = tempDF[tempDF.columns[1]].astype(str) + tempDF[tempDF.columns[2]].astype(str) 
        
        for i in range(len(tempDFMoneyAmount.index)):
            tempString = tempDFMoneyAmount.iloc[i] 
            if (tempString.find('-') > 0 or tempString.find('+')>0):
                pass
            else:
                tempDFMoneyAmount.iloc[i] = '' 
        #######################################################################################################
        #CREATING THE RIGHT TABLE FOR THE DB BEFORE THE CATEGORIZATIONS
        tempDF = pd.DataFrame({ 'date': tempDFDate,'transaction':tempDFExplanation, 'amount':tempDFMoneyAmount})
        tempDF = tempDF.drop(tempDF[tempDF.transaction ==''].index)
        tempDF = tempDF.drop(tempDF[tempDF.amount ==''].index)
        return tempDF
    
    
    def addDataToDb(self, tempDF, fileName):
        filePathFull = fileName.parts

        fileYear = filePathFull[-1].split('.'); fileYear = fileYear[0]; fileYear = fileYear[-4:]
        
        fileName = filePathFull[-1]; fileName = fileName.split('.'); fileName = fileName[0]
        
        sql = ('DECLARE @return_value int, @ans int EXEC @return_value = [dbo].[spCheckIfBatchExists] @ans = @ans OUTPUT, @batchId = '+fileName+' SELECT @ans')
        checkIfOldbatch = int (self.conn.execute(sql).fetchone()[0])
        if checkIfOldbatch != 0:
            print(fileName)
            sql = ('EXEC	[dbo].[spDeleteFromTable]@BatchId ='+fileName)
            self.conn.execute(sql)
            #deleteRowsProcedureBasedOnTheName
        #######################################################################################################

        #check the lastest value from table for serious business 
        for row in tempDF.itertuples():
 
            # populoidaan stage
            self.cursor.execute("INSERT INTO [tilit].[NORDEA_ACCOUNT_STATEMENT_STAGE] VALUES(?,?,?,?,?)",(row.date, row.transaction, row.amount,'0',fileName[0]))
            self.conn.commit()
        #Siirrä seuraavalle taululle
     
        self.cursor.execute('''EXEC[dbo].[spLoadToFinalTableFromStage] @finalTableParam = 'NORDEA_ACCOUNT_STATEMENT_FINAL', @stagetableParam = 'NORDEA_ACCOUNT_STATEMENT_STAGE', @tempYear ='''+str(fileYear)+'')
        self.conn.commit()
        
        #Lisää rivi metatauluun
        now = datetime.now(); current_time = now.strftime("%H:%M:%S")
        print(current_time,fileYear,fileName)
        self.cursor.execute("INSERT INTO [budjettiExcel].[metatiedot].[AJETUT_AJOT] VALUES(?,?,?)",(current_time,fileYear,fileName))
        self.conn.commit()                                

        #Tyhjennä taulu
        self.cursor.execute("TRUNCATE TABLE [tilit].[NORDEA_ACCOUNT_STATEMENT_STAGE]")
        self.conn.commit()                                

            
        ###############################
        
        return 
    
        #print(tempDF)
        #count =  self.getRows()
        #print(count)
        
        # prosa joka tsekkaa onko dataa jo ajettu sisää tolla pv:llä
        #Jos ei ole lisätty vielä kantaan, niin lisää uudet rivit kantaan

        #tempDF.to_excel("output111.xlsx",index=False)
        #print(tempDF)

    def printDbRows(self):
        
        table = self.cursor.execute('SELECT * FROM [NORDEA_ACCOUNT_STATEMENT] ;')
        table = table.fetchall()
        for i in table:
            print(i)
