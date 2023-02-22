#!/usr/bin/env python3

import random
from PyPDF4 import PdfFileReader, PdfFileWriter

with open('original.pdf', 'rb') as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    num_pages = pdf_reader.getNumPages()
    page_numbers = list(range(num_pages))
    random.shuffle(page_numbers)
    pdf_writer = PdfFileWriter()
    for page_number in page_numbers:
        pdf_writer.addPage(pdf_reader.getPage(page_number))
    with open('shuffled.pdf', 'wb') as shuffled_pdf_file:
        pdf_writer.write(shuffled_pdf_file)
