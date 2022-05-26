numbers=[1,2,3,4,5]

first,second,third,fourth,fifth=numbers


# Traditional
# first=numbers[0]
# second=numbers[1]
# third=numbers[2]
# fourth=numbers[3]
# fifth=numbers[4]

print("First",first)
print("Second",second)
print("Third",third)
print("Fourth",fourth)
print("Fifth",fifth)

print("---------------------------------------------")

numbers=[1,2,3,4,4,4,4,4,5,6]


first,second,third,*others,second_last,last=numbers
print("First",first)
print("Second",second)
print("Third",third)
print("Others",others,type(others))
print("Second Last",second_last)
print("Last",last)

print("-------------------------------------------------")

data=(1,"Tom")

index,value=data
print("Index:",index)
print("Value:",value)