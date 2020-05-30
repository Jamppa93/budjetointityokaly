######################################################################
# title: Budjetointityokalu
# authors: Jan Saariniemi & Anssi Lillomäki & Santeri Lipsunen
# date: 30.5.2020
######################################################################
#libraries
import time
import sys
from etlManager import etlManager
from fileHandler import fileHandler
######################################################################
#tic
t = time.time()

class mainClass(): 
    checkNfile = 0
    tempfileName = ''
    fileLocDirectories = []
    etlManagerInst = None
    fileHandlerInst = None
    
    def __init__(self):
        self.checkNfile = 0
        self.tempfileName = ''
        self.fileLocDirectories = ['budjetointityokalu/newFiles','budjetointityokalu/usedFiles','budjetointityokalu/dbFile']  
        self.etlManagerInst = etlManager()
        self.fileHandlerInst = fileHandler()
    
    def getFileLocDirectories(self):
        return(self.fileLocDirectories)
                           
    
######################################################################
main = mainClass()



print(main.getFileLocDirectories())
main.fileHandlerInst.printObjectType()
main.etlManagerInst.printObjectType()


#toc
print((time.time() - t))



