# input and other variables
octNum = input("Enter a string of octal digits: ")
decNum = 0
exponent = len(octNum) - 1

# conversion
for octDigit in octNum:
    conversion = int(octDigit) * 8 ** exponent
    decNum += conversion
    exponent -= 1

# output
print("The integer value is", decNum)
