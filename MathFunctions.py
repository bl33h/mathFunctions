#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: Math Functions
    # @version: I
    #- Creation: 01/08/2022
    #- Last modification: 17/08/2022

# Imports
from array import *

# Boolean       
keepGoing = True

# While cycle for the menu
while keepGoing:
    print("--- What would you like to do? ---")
    print("1. Spread function.")
    print("2. Pseudorandom number generator.")
    
    option = input("\nType the number that corresponds to the option you wanna execute: ")
    
    # First option || Spread function & hash
    if option == "1":
        arr = array ('i', [])
        n = int(input("Enter the length of the array: "))
        for i in range(n):
            y = int(input("Enter the next value: "))
            arr.append(y)
        div = 12
        arr = list(map(lambda x: x % div, arr))
        finalArr = []
        print(finalArr)

    # Second option || Pseudorandom number generator
    elif option == "2":
        print("\n")

    else:
        print("\nERROR: Please type a valid option.")