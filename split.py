#!/usr/bin/python3
import os, getopt, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
            
def three(in_name, out_name):
	split(in_name, out_name)
	
def two(in_name):
	split(in_name, 'PDF_Page')
	
def one():
	print('Please add the file name of the PDF you wish to split')

if __name__ == '__main__':
	args = len(sys.argv)
	if (args == 3):
		three(sys.argv[1],sys.argv[2])
	if (args == 2):
		two(sys.argv[1])
	if (args == 1):
		one()
