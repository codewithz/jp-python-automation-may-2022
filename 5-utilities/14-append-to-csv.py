import csv

with open("data_products.csv", "a") as file:
    writer = csv.writer(file)

    data = [1010, 25, 34]

    writer.writerow(data)
