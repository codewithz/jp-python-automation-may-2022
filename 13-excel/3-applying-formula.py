import openpyxl

wb = openpyxl.load_workbook("myfile.xlsx")
ws = wb['Sheet1']

formula = '=SUM(A2:A8)'

ws['A10'] = formula

wb.save("myfile.xlsx")
