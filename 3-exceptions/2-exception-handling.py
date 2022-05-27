try:
    age=int(input("Enter Age:"))
    print(f"Age is {age}")
except ValueError as ex:
    print("You seem to have entered wrong age")
    print(ex)
else:
    print("Else is executed only when no exception occurs")


print("Execution continues.....")
