message="Hello All"

def greet(name):
    message="Hello"
    print(name)

def send_email():
    global message;
    message="Hi"




print(message)
greet("Zartab")
print(message)
send_email()
print(message)