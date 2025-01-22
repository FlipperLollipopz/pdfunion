import os
from PyPDF2 import PdfMerger

def union_pdf():
    merger = PdfMerger()
    cartella_input = os.getcwd()
    file_pdf = [
        os.path.join(cartella_input, f) for f in os.listdir(cartella_input) if f.endswith('.pdf')
    ]
    file_pdf.sort()
    for file in file_pdf:
        print(f"Adding: {file}")
        merger.append(file)
    merger.write("UnionResult.pdf")
    merger.close()

union_pdf()
