import os
from PyPDF2 import PdfMerger

def combine_pdfs(directory, output_filename):
    # Initialize PdfMerger object
    merger = PdfMerger()

    # Get a list of all PDF files in the directory with their full paths
    pdf_files = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(".pdf")]

    # Sort the list of PDF files by modification date
    pdf_files.sort(key=os.path.getmtime)
    print(pdf_files)
    # Append each PDF to the merger object in sorted order
    for filepath in pdf_files:
        merger.append(filepath)

    # Write the combined PDF to the output file
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    # Close the merger object
    merger.close()

# Example usage
combine_pdfs("/Users/hiteshbandhu/Downloads/docs-pdf", "combined_output.pdf")
