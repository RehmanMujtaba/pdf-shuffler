# PDF Shuffler

PDF Shuffler is a simple Python script that shuffles the pages of a PDF file and creates a new PDF file with the shuffled pages. The script uses the PyPDF2 or PyPDF4 library to manipulate the PDF files.

## Features

- Shuffle the pages of a PDF file randomly
- Create a new PDF file with the shuffled pages
- Easy to use and modify
- Supports Python 2.7 and 3.x (PyPDF2) or Python 3.10 and higher (PyPDF4) (replace in import line)

## Usage

To use PDF Shuffler, simply run the script from the command line and specify the path to the input PDF file and the path to the output PDF file:
```
python pdf_shuffler.py input.pdf output.pdf
```

The script will shuffle the pages of the input PDF file and save the shuffled pages to the output PDF file.

## Installation

PDF Shuffler requires the PyPDF2 or PyPDF4 library to be installed. You can install the library using pip:
```
pip install pypdf2 # for Python 2.7 and 3.x
pip install pypdf4 # for Python 3.10 and higher
```
