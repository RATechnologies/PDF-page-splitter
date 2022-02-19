#!/usr/bin/python3
import os, getopt, sys
import tkinter as tk
from tkinter import filedialog
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

if __name__ == '__main__':

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename( title = "Select a File", filetypes = (("PDF files", "*.pdf"), ("all files","*.*")))
    two(file_path)
