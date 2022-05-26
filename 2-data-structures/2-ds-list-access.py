letters=["a","b","c","d","e"]
print(letters)

# Access the first element
print(letters[0])

# Access the last element
print(letters[-1])

# Access in Ranges
print(letters[0:2])
print(letters[:3])
print(letters[2:])

# Clone
letters_clone=letters[:]
print("Clone:",letters_clone)

# Steppers

numbers=list(range(1,21))
print(numbers[1:20:2])
print(numbers[::-1])
print(numbers[::-2])