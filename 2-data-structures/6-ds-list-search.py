letters=["a","b","c","d","e"]

print(letters.index("b"))
# print(letters.index("z"))
# # ValueError: 'z' is not in list

# Way 1: TO search without breaking the prpgram

if 'g' in letters:
    print(letters.index('g'))

# Way 2 - To Search without breaking the program

d_count=letters.count("d")

if d_count>0:
    print(letters.index("d"))