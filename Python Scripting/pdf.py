import PyPDF2
import sys

inputs = sys.argv[1:]

# # Basic PDF operations
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('rotated.pdf', 'wb') as new_file:
#         writer.write(new_file)

# # Merging PDFs
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('combined.pdf')


# pdf_combiner(inputs)

# Open watermark pdf
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

# Loop through other PDFs
for pdf in inputs:

    pdfReader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through pages
    for pageNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        # Overlay watermark on page
        page.mergePage(watermark.getPage(0))
        pdfWriter.addPage(page)

    # Save output pdf
    with open(f'watermarked_{pdf}', 'wb') as file:
        pdfWriter.write(file)
