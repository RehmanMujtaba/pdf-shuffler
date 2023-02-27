#!/usr/bin/env python3

import random
from PyPDF4 import PdfFileReader, PdfFileWriter

# file name = original.pdf
with open('original.pdf', 'rb') as pdf_file:
    
    # Open File
    pdf_reader = PdfFileReader(pdf_file)
    
    # Create a list of page numbers
    num_pages = pdf_reader.getNumPages()
    page_numbers = list(range(num_pages))
    
    # Shuffle the page numbers
    random.shuffle(page_numbers)
    
    # Create a new pdf with the shuffled pages
    pdf_writer = PdfFileWriter()
    for page_number in page_numbers:
        pdf_writer.addPage(pdf_reader.getPage(page_number))
    with open('shuffled.pdf', 'wb') as shuffled_pdf_file:
        pdf_writer.write(shuffled_pdf_file)
