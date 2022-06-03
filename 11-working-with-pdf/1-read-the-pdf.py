import PyPDF2

with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    print(page.extractText())
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    # writer.insertPage(page, 1)
    # writer.insertBlankPage()
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
