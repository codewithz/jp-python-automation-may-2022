for number in range(5):
    print(number)

print("Execution Completed..")

print("-----------------------------------")


for number in range(1,4):
    print("Attempt",number,(number*'.'))


print("-------------------------------------------")

# for...else

successful=True

for number in range(1,6):
    print("Attempting to send a message")
    if number==2 and successful:
        print("Message sent successfully")
        break
else:
   print("Attempted for 5 times and failed")

# if the for loop completes without breaking in between, else will come into action
#  