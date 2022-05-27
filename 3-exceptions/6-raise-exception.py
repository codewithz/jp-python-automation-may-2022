def calculate_xfactor(number):
    if number<=0:
        raise ValueError("Number cannot be zero or less")
    return 10/number


# ---------------------------------------------

try:
    number=int(input("Enter a number:"))
    xfactor=calculate_xfactor(number)
    print("XFactor:",xfactor)
except ValueError as ex:
    print(ex)

