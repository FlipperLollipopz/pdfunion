import os
from pypdf import PdfReader, PdfWriter

def union_pdf():
    cwd = os.getcwd()
    pdfs = [
        os.path.join(cwd, f) for f in os.listdir(cwd) if f.endswith('.pdf')
    ]
    pdfs.sort()
    writer = PdfWriter()
    for pdf in pdfs:
        reader = PdfReader(pdf)
        if not reader.is_encrypted:
            print(f"Adding: {os.path.basename(pdf)[:-4]}")
            writer.append(pdf)
        else:
            print(f"{os.path.basename(pdf)[:-4]} is encrypted")
        reader.close()
    file = open("UnionResult.pdf", 'wb')
    writer.write(file)
    file.close()
    writer.close()

union_pdf()
