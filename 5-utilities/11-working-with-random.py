import random
import string

print(random.random())

print(random.randint(10, 25))


print(random.choice([10, 23, 34, 45, 56, 67, 78, 89, 91]))

print(random.choices([10, 23, 34, 45, 56, 67, 78, 89, 91], k=2))

combined = string.ascii_letters+string.digits+string.punctuation

print("------------------------------------------------------------")

print("List:", combined)

print("------------------------------------------------------------")


def generate_random_password():
    random_password = "".join(random.choices(
        string.ascii_letters+string.digits+string.punctuation, k=6))
    return random_password


for x in range(1, 6):
    print(generate_random_password())
