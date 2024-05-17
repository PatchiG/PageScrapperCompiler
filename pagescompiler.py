import os
from PyPDF2 import PdfFileReader, PdfMerger

def get_page_number(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        return reader.numPages

def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    pdf_files.sort(key=lambda x: int(x.split('-')[-1].split('.')[0]))  # Sort files based on page numbers

    for filename in pdf_files:
        filepath = os.path.join(input_folder, filename)
        merger.append(filepath)

    merger.write(output_file)
    merger.close()

# Example usage
input_folder = '/content/downloaded_pages'
output_file = 'knowledge_test_merged.pdf'
merge_pdfs(input_folder, output_file)
