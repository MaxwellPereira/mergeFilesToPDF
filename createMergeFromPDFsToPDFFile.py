#pip install PyPDF2
import os
from PyPDF3 import PdfFileReader, PdfFileMerger

files_dir = ".\\pdfs\\"
pdf_files = [f for f in os.listdir(files_dir) if f.endswith("pdf")]
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(files_dir, filename), "rb"))
merger.write(os.path.join(".\\output\\", "pdfs_merged_full.pdf"))