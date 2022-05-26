letters=["a","b","c","d","e"]

for letter in letters:
    print(letter)

print("----------------------------------")

for element in enumerate(letters):
    print(element)
    print(type(element))

print("----------------------------------")

data=(1,"Tom")
index,value=data
print("Index:",index)
print("Value:",value)
print("----------------------------------")

for index,value in enumerate(letters):
    print(index,"-",value)
