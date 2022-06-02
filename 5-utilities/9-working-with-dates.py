from datetime import datetime
import time

date1 = datetime(2022, 6, 2)
print(date1)

current_date = datetime.now()
print(current_date)

date_in_string = "23/04/2021"

date2 = datetime.strptime(date_in_string, "%d/%m/%Y")
print(date2)

current_time = time.time()
print("Timestamp:", current_time)
date3 = datetime.fromtimestamp(current_time)
print("Date from Timestamp:", date3)

print("Date:", current_date)
print("Formatted Date:", current_date.strftime("%d-%m-%Y"))
