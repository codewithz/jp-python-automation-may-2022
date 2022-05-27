import time;

print(time.time())

def send_email():
    for x in range(10000):
        print(x)



start=time.time()
send_email()
end=time.time()

duration=end-start
print("Duration:",duration)