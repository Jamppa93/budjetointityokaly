


import tabula

#https://medium.com/@umerfarooq_26378/python-for-pdf-ef0fac2808b0

class fileHandler(): 

    def printObjectType(self):
        print(type(self))

    def readPdf(self,filePath):
        tempfileList = tabula.read_pdf(filePath,multiple_tables=True, pages='all')    
        print(type(tempfileList))  
        return tempfileList


######################################################################################################
#OLD STUFF:  ANOTHER PDF READER. DOES NOT DIVIDE THE ELEMENTS AS WELL AS TABULA LIB.

# import PyPDF2


#        tempfileList = []
#        pdfFileObj = open(filePath, 'rb')
#        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#        for i in range(pdfReader.numPages):
#            pageObj = pdfReader.getPage(i)
#            tempfileList.append(pageObj.extractText())
######################################################################################################
# TABULA INSTRUCTIONS:  SOME VERY BASIC STUFF

        #print(df)
        #print(len(df))
        #print(df[0]) -- TULOSTAA ENSIMMÄISEN SIVUN
        
        # convert PDF into CSV file
        #tabula.convert_into(filePath, "output.csv", output_format="csv",pages='all')
        
        
        #tempfileList = tabula.read_pdf(filePath,multiple_tables=True, pages='all')
        #tempfileList = tabula.read_pdf(filePath,multiple_tables=True, pages='all')
        # -->   IS A LIST
        #print(type(df))
        #for i in df:
         #   print(i)
        
        

######################################################################################################