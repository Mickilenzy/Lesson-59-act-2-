number = int(input("Enter a number:"))
binary = bin(number)[2:]
print("Binary is :", binary)

n = int(input("Which bit number do you want ot see? (1 = first from left):"))
if 1 <= len(binary):
    bit = binary[n-1]
    print("That bit is:", bit)

else:
    print("OOOPS! Bit number too big.")    