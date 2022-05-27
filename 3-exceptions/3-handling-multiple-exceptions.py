try:
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age} and XFactor is {xfactor}")
    numbers=[1,2]
    print(numbers[3])
except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError as ex:
    print("You seem to have entered age as zero")
except Exception as ex:
    print("Some exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred..")


print("Execution continues.......")