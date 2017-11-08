from PyPDF2 import PdfFileReader, PdfFileMerger
import os

pdf_files = [f for f in os.listdir('.') if f.endswith('pdf')]

final_name = input("Enter the name of file to be generated: ")

merger = PdfFileMerger()

for filenames in pdf_files:
    merger.append(PdfFileReader(os.path.join('.', filenames)), 'rb')

print("These following will be merged into %s.pdf" % (str(final_name)))

input("Press any key to continue OR 'CTRL+C' to cancel..")

merger.write(os.path.join('.', str(final_name) + ".pdf"))

print("Successfully merged all pdf file into %s.pdf" % (str(final_name)))