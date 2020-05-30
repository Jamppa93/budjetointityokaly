######################################################################
# title: Budjetointityokalu
# authors: Jan Saariniemi & Anssi Lillomäki & Santeri Lipsunen
# date: 30.5.2020
######################################################################
#libraries
import time
######################################################################
#tic
t = time.time()

class mainClass(): 
    checkNfile = 0
    tempfileName = ''
    fileLocDirectories = []
    
    def __init__(self):
        self.checkNfile = 0
        self.tempfileName = ''
        self.fileLocDirectories = ['budjetointityokalu/newFiles','budjetointityokalu/usedFiles','budjetointityokalu/dbFile']  
    
    def getFileLocDirectories(self):
        return(self.fileLocDirectories)
                           
              
######################################################################
main = mainClass()
print(main.getFileLocDirectories())



#toc
print((time.time() - t))



