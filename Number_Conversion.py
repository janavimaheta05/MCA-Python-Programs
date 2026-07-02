print("========== NUMBER SYSTEM CONVERTER ==========")
print("1. Decimal to Binary")
print("2. Decimal to Octal")
print("3. Decimal to Hexadecimal")
print("4. Binary to Decimal")
print("5. Octal to Decimal")
print("6. Hexadecimal to Decimal")
print("7. Character to Unicode")
print("8. Unicode to Character")

ch= int(input("Enter your choice (1-8)=> "))

if ch == 1:
    num = int(input("Enter Decimal Number: "))
    print("Binary =", bin(num))

elif ch == 2:
    num = int(input("Enter Decimal Number: "))
    print("Octal =", oct(num))

elif ch == 3:
    num = int(input("Enter Decimal Number: "))
    print("Hexadecimal =", hex(num).upper())

elif ch == 4:
    binary = input("Enter Binary Number: ")
    print("Decimal =", int(binary, 2))

elif ch == 5:
    octal = input("Enter Octal Number: ")
    print("Decimal =", int(octal, 8))

elif ch == 6:
    hexa = input("Enter Hexadecimal Number: ")
    print("Decimal =", int(hexa, 16))

elif ch == 7:
    c = input("Enter a Character: ")
    print("Unicode Value =", ord(c))

elif ch == 8:
    num = int(input("Enter Unicode Value: "))
    print("Character =", chr(num))

else:
    print("Invalid Choice!")