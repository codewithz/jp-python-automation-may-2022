class ValueTooLargeError(Exception):
    """Raised when the input value is large"""
    pass


class ValueTooSmallError(Exception):
    """Raised when the input value is small"""
    pass

# ----------------------------------------------------

number=12;
# Number user need to guess 

# User will guess a number. 
# If the number is lower than one should be guessing throw ValueTooSmallError
# If the number is greater than one should be guessing throw ValueTooLargeError
# If the number is correct, say correct value and exit

while True:
    try:
        incoming_number=int(input("Guess the number:"))

        if incoming_number<number:
            raise ValueTooSmallError
        elif incoming_number>number:
            raise ValueTooLargeError
        else:
            break
    except ValueTooLargeError:
        print("Entered value is large. TRY AGAIN!!")
    except ValueTooSmallError:
        print("Entered value is small. TRY AGAIN!!")

print("Congratulations..")