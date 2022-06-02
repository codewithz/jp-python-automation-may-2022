import csv

with open("data_products.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 15])
    writer.writerow([1001, 10, 23])
    writer.writerow([1002, 12, 43])
    writer.writerow([1003, 21, 12])
    writer.writerow([1004, 35, 98])
