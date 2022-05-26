cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

print("-----------------------------------------")

prices=list(map(lambda element:element[1],cart))
print("Prices using Lambda:",prices)

print("-----------------------------------------")

# [expression for item in items]

prices_lc=[element[1] for element in cart] 

print("Prices using List Comprehension:",prices_lc)


print("-----------------------------------------")

filtered_list=list(filter(lambda element:element[1]>=5,cart))
print("Filtered List:",filtered_list)

# [expression for item in items if condition]

filtered_list=[(name,price) for name,price in cart if price>=5]
print("Filtered using List Comprehension",filtered_list)
