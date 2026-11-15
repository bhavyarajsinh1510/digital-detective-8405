

number = int(input("Enter a positive decimal number: "))

if number <= 0:
    print("Please enter a positive number.")
else:
    binary_number = bin(number)
    hexadecimal_number = hex(number)

    print("Decimal:", number)
    print("Binary:", binary_number[2:])
    print("Hexadecimal:", hexadecimal_number[2:].upper())
