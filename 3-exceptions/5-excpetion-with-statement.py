try:
    with open("data.txt") as source,open("emp.txt") as target:
        x=10/1
        print("Some operation inside with block")
        print("Source File is closed?:",source.closed)
        print("Target File is closed?:",target.closed)
        print("-------------Last line of with block--------")
    
    print("---------- Outside the with block-----------")
    print("Source File is closed?:",source.closed)
    print("Target File is closed?:",target.closed)
except Exception as ex:
    print(ex)
else:
    print("No exception occured")
finally:
    print("House Keeping Code")
    