from cgitb import reset
from email import message
from operator import mul
import re


print("----------- Normal Function ------------------")

def greet():
    print("Hi there")
    print("Welcome Aboard")


greet()

print("--------------- Functions with parameters------------")

def greeting(first_name,last_name):
    print(f"Hello {first_name} {last_name}")

greeting("Zartab","Nakhwa")
greeting("Mike","Holding")

print("-------- Functions with Return Types -----------")

# Types of Function

# 1. Perform a Task
# 2. Do some processing and return a value 

# 1. Perform a Task:

def greet(name):
    print(f"Hello {name}")

greet("Zartab")
# ----------------------------------------------------
def get_greeting(name):
    greeting=f"Hi {name.upper()}"
    return greeting

message=get_greeting("Alex")

# Send this in an email
# Print in log
# Store in DB
# Send over a network

print("DEBUG:",message)

print("--------------- Function with keyword arguments---------")


def increment(number,by):
    number=number*3;
    added_values=number+by;
    return added_values



result=increment(2,5)
print(result)

result=increment(by=3,number=7)
print(result)

print("--------------- Default Arguments-----------------")

def increment_number(number,by=1):
    return number+by


result=increment_number(number=5)
print(result)

result=increment_number(by=3,number=5)
print(result)

print("--------------- Varying Arguments [xargs]-------------")

def multiply(*numbers):
    print(numbers,type(numbers))
    total=5
    for number in numbers:
        total=total*number
    
    return total

print(multiply(1,2,3,4,5))

print(multiply(3,4,8))

print("------------ Varying Arguments for Dict -- [xxargs/kwargs]-----")

def save_user(**user):
    print(user)
    print(type(user))

save_user(id=1,name='Tom',dept='IT',salary=30000.45)
