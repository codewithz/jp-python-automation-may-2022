from datetime import datetime, timedelta

date1 = datetime(2020, 1, 1)+timedelta(days=10, seconds=30)
date2 = datetime.now()

duration = date2-date1
print(duration)

print("Days:", duration.days)
print("Seconds:", duration.seconds)
print("Seconds-Total:", duration.total_seconds())
