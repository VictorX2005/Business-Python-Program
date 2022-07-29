# import modules
from curses.ascii import isalpha
from operator import truediv
from pickle import TRUE
from xmlrpc.client import boolean


# validates that the inputted name is in the alphabet
def verifyName(name):
    valid = True
    while(valid):
        try:
            assert name.isalpha()
            valid = False
        except:
            print("Invalid name, must be letters only.")
            name = input("Try Again: ")
    return name

# validates that the inputted number is a number and is 10 digits
def verifyNumber(number):
    valid = True
    while(valid):
        try:
            assert number.isnumeric()
            assert len(str(number)) == 10
            valid = False
        except:
            print("Invalid number, must be 0-9 and 10 digits")
            number = input("Try Again: ")
    return number
        
# verifies that the package number is between 1-3
def verifyPackage(package):
    valid = True
    while(valid):
        try:
            assert package < 4 | package > 0
            valid = False
        except:
            print("Invalid number, must be between 1-3")
            package = int(input("Try Again: "))
    return package  

# adds the cost to bill depending on package chosen
def addBill(package):
    if package == 1:
        return "$50"
    elif package == 2:
        return "$75"
    elif package == 3:
        return "$100"