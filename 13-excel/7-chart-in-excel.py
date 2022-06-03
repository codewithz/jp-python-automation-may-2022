
import openpyxl
from openpyxl.chart import DoughnutChart, Reference

from openpyxl.chart.series import DataPoint

wb = openpyxl.Workbook()

ws = wb.active

data = [
    ['Pie', 2014],
    ['Plain', 40],
    ['Jam', 2],
    ['Lime', 20],
    ['Chocolate', 30]
]

for row in data:
    ws.append(row)


chart = DoughnutChart()

labels = Reference(ws, min_col=1, min_row=2, max_row=5)
data = Reference(ws, min_col=2, min_row=1, max_row=5)

chart.add_data(data, titles_from_data=True)

chart.set_categories(labels)

chart.title = "Doughnut Charts"

chart.style = 26

ws.add_chart(chart, 'E1')

wb.save('doughnut.xlsx')
