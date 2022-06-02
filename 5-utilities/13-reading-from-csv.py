import csv

with open("aadhaar_data.csv") as file:
    reader = csv.reader(file)
    print(type(reader))

    max_rows = 10
    rows_read = 0
    for row in reader:
        print(row)
        rows_read = rows_read+1
        if rows_read > max_rows:
            break
