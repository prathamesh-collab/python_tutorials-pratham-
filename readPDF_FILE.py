#/usr/bin/env python


import PyPDF2
pdffileobj = open('academic calendar 2019-29_1.pdf','rb')
   
pdfReader = PyPDF2.PdfFileReader(pdffileobj)
pageobj = pdfReader.getPage(0)
text = pageobj.extractText()
print(text)




