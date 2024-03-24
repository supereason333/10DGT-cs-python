import math

def get_check_digit(input):
    input = str(input)
    sum1 = 0
    sum2 = 0
    for i in range(0, 12, 2):
        sum1 += int(input[i])
    for i in range(1, 13, 2):
        sum2 += int(input[i])
    sum2 = int(str(sum2)[len(str(sum2)) - 1]) * 3                                   # get the last digit of sum2 and times it by 3
    total = int(str(sum2)[len(str(sum2)) - 1]) + int(str(sum1)[len(str(sum1)) - 1]) # adds the last digit of sum1 and sum2
    check = 10 - int(str(total)[len(str(total)) - 1])                               # subtracts the last digit of the total from 10
    return check

print("1 - Text to ASCII code\n2 - ASCII code to Text\n3 - Caesar cipher\n4 - GTIN 13 barcode checker")
option = int(input())

if (option == 1):   # Text to ASCII code
    input = input("Enter text: ")
    for i in input:
        print(ord(i), end=" ")      # ends each ascii code with a space

elif (option == 2): # ASCII code to Text
    input = input("Enter ASCII code: ")
    input = input.split(" ")        # splift the input into a list at every space
    for i in input:
        print(chr(int(i)), end="")

elif (option == 3): # Caesar cipher
    input = input("enter text: ").lower()
    shift = int(input())
    for i in input: 
        if (ord(i) + shift > 122):  # if the shift goes beyond 'z'
            print(chr(ord(i) + shift - 26), end="")
        elif (ord(i) + shift < 97): # if the shift goes below 'a'
            print(chr(ord(i) + shift + 26), end="")
        else:                       # if the shift is withen 'a' and 'z'
            print(chr(ord(i) + shift), end="")

elif (option == 4): # GTIN 13 barcode checker
    input = input("Enter Barcode: ")
    if (len(input) == 12):          # Finding the check digit
        check = get_check_digit(input)
        print ("The check digit is: " + str(check))
        print (str(input) + str(check))
    elif (len(input) == 13):        # Checking the barcode
        if (input[12] == str(get_check_digit(math.floor(int(input) / 10)))):
            print ("The barcode is correct")
        else:
            print ("The barcode is incorrect")