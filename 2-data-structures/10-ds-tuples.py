# Tuples- are the read only list
# ()

# Ways to define a tuple 

point=(1,2)
print(point)
print(type(point))

point=1,
print(point)
print(type(point))

point=1,2
print(point)
print(type(point))

point=(1,2)+(3,4)
print(point)

point=(1,2)*3
print(point)

print("------------ Accessing elements in tuple --------------")

point=(1,2,3)
print("Index:",point[1])
print("Range Access:",point[0:2])

print("------------ Unpacking elements in tuple --------------")

x,y,z=point

print("X:",x)
print("Y:",y)
print("Z:",z)

print("------------ Searching elements in tuple --------------")
if 10 in point:
    print("10 is in the tuple")
else:
    print("10 is not in tuple")

print("------------ Tuples are immutable --------------")
# point[1]=10
# TypeError: 'tuple' object does not support item assignment
