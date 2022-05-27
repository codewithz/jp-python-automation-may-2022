try:
    file=open("data.txt")
    print("Is the File Closed? :",file.closed)
    age=int(input("Enter Age:"))
    xfactor=10/age
    print(f"Age is {age} and XFactor is {xfactor}")
    
except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError as ex:
    print("You seem to have entered age as zero")
except Exception as ex:
    print("Some exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred..")
finally:
    print("Executes in all conditions [In case of exception or no exception]")
    file.close()
    print("Is the File Closed? :",file.closed)
   