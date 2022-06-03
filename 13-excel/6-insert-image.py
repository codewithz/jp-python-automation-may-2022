import openpyxl

from openpyxl.drawing.image import Image

wb = openpyxl.load_workbook('myfile.xlsx')
ws = wb['Sheet1']

img = Image('logo.jpg')
ws['A14'] = 'Adding Image'
img.width = 225
img.height = 225

ws.add_image(img, 'B15')

wb.save('myfile.xlsx')
