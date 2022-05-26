# Set --> No Duplicates | Unordered
# {}

numbers={1,1,1,2,3,4,4}
print(numbers)

numbers_list=[5,5,6,6,7,7,8,8,8]
unique_set={*numbers_list}
print(unique_set)

first={1,2,3,4}
print("First:",first)

second={1,4,5}
print("Second:",second)

second.add(6)
print("Second:",second)

second.add(5)
print("Second:",second)

second.remove(4)
print("Second:",second)

# second.remove(4)
# print("Second:",second)
# KeyError: 4

second.discard(4)
print("Second:",second)

print("-------------- Set OPerations--------------------")
print("First:",first)
print("Second:",second)

print("Union:",first.union(second))
print("Union:",first | second)

print("Intersection",first.intersection(second))
print("Intersection",first & second)

print("Difference",first.difference(second))
print("Difference",first - second)

print("Difference",second.difference(first))
print("Difference",second - first)

print("Symmetric Difference",first.symmetric_difference(second))
print("Symmetric Difference",first ^ second)



