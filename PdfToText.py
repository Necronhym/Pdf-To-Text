from pdf2image import *
import pytesseract
import sys
import os
from PyPDF2 import PdfFileReader
path= str(sys.argv[1:])[2:-2]
pdf = PdfFileReader(open(path,'rb'))
pages = pdf.getNumPages()
lan = 'en'
f = open(path.rsplit(".", 1)[0] + ".txt", 'a')
for i in range(1, pages+1):
	image = convert_from_path(path, first_page=i, last_page=i)
	print("Converting page: "+ str(i) + "/" + str(pages));
	say = pytesseract.image_to_string(image[0]);
	f.write(say+"\n")
	f.flush()
print("Conversion of " + path + " Complete")
