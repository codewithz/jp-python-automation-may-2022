cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

# ---------------------------

# def sort_cart(element):
#     return element[1]

# cart.sort(key=sort_cart)
# --------------------------

cart.sort(key=lambda element:element[1])
print("Sorted:",cart)

print("---------------------Mapping--------------------------")

prices=[]

for name,price in cart:
    prices.append(price)

print("Prices:",prices)

def get_price(element):
    return element[1]

my_prices=list(map(get_price,cart))

print("Price List:",my_prices)

prices=list(map(lambda element:element[1],cart))

print("Price List using lambda:",prices)

print("---------------------Filtering--------------------------")

filtered_list=[]

for name,price in cart:
    if price>=5:
        filtered_list.append((name,price))

print("Manual:",filtered_list)

def check_price(element):
    return element[1]>=5;

filtered_list_1=list(filter(check_price,cart))
print("Filtered List:",filtered_list_1)

filtered_list_2=list(filter(lambda element:element[1]>=5,cart))
print("Filtered List using lamda",filtered_list_2)