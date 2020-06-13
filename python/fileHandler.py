
import PyPDF2
#https://medium.com/@umerfarooq_26378/python-for-pdf-ef0fac2808b0

class fileHandler(): 


    def printObjectType(self):
        print(type(self))
  

    def readPdf(self,filePath):
        
        pdfFileObj = open(filePath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(i)
            print(pageObj.extractText())
        
        


