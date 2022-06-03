import PyPDF2

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]

for file in file_names:
    merger.append(file)

merger.write("combined.pdf")
