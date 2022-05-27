from sys import getsizeof

values=[x*2 for x in range(1000)]
print("Size of Generated Value",getsizeof(values))
print(values)

print("--------------------------------------")

values=(x*2 for x in range(100000000000))
print("Size of Generated Value",getsizeof(values))
print(values)

for number in values:
    print(number)