######################################################################
# title: Budjetointityokalu
# authors: Jan Saariniemi & Anssi Lillomäki & Santeri Lipsunen
# date: 30.5.2020
######################################################################
#libraries
import time
import sys
import pathlib # https://docs.python.org/3/library/pathlib.html#module-pathlib
from etlManager import etlManager
from fileHandler import fileHandler
######################################################################
#MainClass
class mainClass(): 
    checkNfile = [] # muutetaan listaksi
    tempfileName = ''
    fileLocDirectories = []
    etlManagerInst = None
    fileHandlerInst = None
    
    def __init__(self):
        self.checkNfile = []
        self.tempfileName = ''
        self.fileLocDirectories = ['newFiles','usedFiles','dbFile']  
        self.etlManagerInst = etlManager()
        self.fileHandlerInst = fileHandler()
        
    def getRecentCheckNfile():
        pass
    
    def getNewFilesPath(self):
        return self.fileLocDirectories[0]
    
    def getoldFilesPath(self):
        return self.fileLocDirectories[1]
    
    def getdbPath(self):
        return self.fileLocDirectories[2]
    
    def isFileStructureOk(self):
        fileStructureIsOk = True
        tempList = []
        
        for i in self.fileLocDirectories:
            tempList.append(pathlib.Path(pathlib.Path(__file__).parents[1].absolute(), i))

        for i in tempList:
            if i.is_dir() == False: #path doesn’t exist, is a broken symlink  or it is not a regular file
                fileStructureIsOk = False
                break 
            
        if  fileStructureIsOk == True:
            self.fileLocDirectories = tempList  #replace the filedirectory paths 
        return fileStructureIsOk




    def getRecentNewFileNamesToList(self):
        
        path = pathlib.Path(self.getNewFilesPath())
        tempList = []
        for fileDir in path.rglob('*.pdf'):
            tempList.append(fileDir)
        #Should do somehting to files which are not pdf. tyyliin clear all tai jotain mut ois tehtävä vasta lopussa
        return tempList




    def startProcess(self):
        
        
        
        #print(self.getNewFilesPath())
        self.checkNfile = self.getRecentNewFileNamesToList()
        #print(self.checkNfile)
        fileCount = len(self.checkNfile)
        while (fileCount>0):
            print(self.checkNfile[fileCount-1])
            tempFile = self.fileHandlerInst.readPdf(self.checkNfile[fileCount-1])
            ## main.etlManagerInst.etlFile(tempFile)
            fileCount -=1 

        ##clearAllFromNewFilesFolder() tai joku tämmönen

  
######################################################################
#MainProgram 

def mainProg():
    main = mainClass()
    isItGo =main.isFileStructureOk()
    if (isItGo == False):
        print("Programs's file structure is not correct: some program files (such as 'newFiles','usedFiles','dbFile) are missing.") #error1 for ErrorObj
    else:
        main.startProcess()
    
######################################################################
#EXECUTE
#tic
t = time.time()
###################################
mainProg()
###################################
#toc
print((time.time() - t))
######################################################################



