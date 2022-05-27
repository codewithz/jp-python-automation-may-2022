# Dictionary
# Key- Value Pair
# {key:value,key:value}
# Keys are unique, if you repeat a key, key used in last will be the one used
# Key can either be int or string

point={"x":1,"y":2}
print(point)
print(type(point))

point=dict(x=1,y=2)
print(point)

print("------------------ Manipulating the Data -------------------------")
point["x"]=10
point["y"]=20
point["z"]=30

point["x"]=100

print(point)

print("----------- Accessing the Data -------------------------")

print("X:",point.get("x"))
print("A:",point.get("a",0))
print(point)
# point.get("key","default value in case the key is not found")
point["a"]=500
print("A:",point.get("a",0))

print("----------- Looping through a dictionary-------------")

for item in point:
    print(item)

print("-------------------------------------------------------")

for key in point:
    print(key)

print("-------------------------------------------------------")

for item in point.items():
    print(item)

print("-------------------------------------------------------")

for key,value in point.items():
    print(key,"-->",value)


# -------------------------------------------------------------
print("-------------------------------------------------------")
square_dict=dict()

# Run a loop from 1 to 20
# Make the current number your key and square of that number as value 

# {1:1,2:4,3:9,.....}

for number in range(1,21):
    square_dict[number]=number*number



print(square_dict)

print("-------------------------------------------------------")
#Dictionary Comprehension

# square_dict={key:value for item in items}
square_dict={number:number*number for number in range(1,21)}
print(square_dict)

# ----------------------------------------------------
print("-------------------------------------------------------")
# items a are in dollars

price_in_usd={"milk":1.02,"coffee":2.3,"bread":2.1}

dollar_to_inr=77.23

price_in_inr={item:round(price*dollar_to_inr,2) for (item,price) in price_in_usd.items()}

print(price_in_inr)


