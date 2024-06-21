import os
from PyPDF2 import PdfMerger

def combine_pdfs(directory, output_filename):
    # Initialize PdfMerger object
    merger = PdfMerger()

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory, filename)
            # Append the PDF to the merger object
            merger.append(filepath)

    # Write the combined PDF to the output file
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    # Close the merger object
    merger.close()

# Example usage
combine_pdfs("/Users/hiteshbandhu/Downloads/docs-pdf", "combined_output.pdf")