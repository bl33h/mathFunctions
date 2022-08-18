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
    print("\n")
    print("--- What would you like to do? ---")
    print("1. Spread function.")
    print("2. Pseudorandom number generator.")
    
    option = input("\nType the number that corresponds to the option you wanna execute: ")
    
    # First option || Spread function & hash
    if option == "1":
        arr = []
        div = int(input("Enter the value for the module (divider): "))
        n = int(input("Enter the length of the array: "))
        for i in range(n):
            y = int(input("Enter the next value: "))
            arr.append(y)

        # Set of the elements
        firstSet = arr
        secondSet = [0 for i in range(div)]
        for i in range(len(arr)):
            s = int(firstSet[i])%int(div)
            if secondSet[s] == 0:
                secondSet[s] = firstSet[i]

    # Second option || Pseudorandom number generator
    if option == "2":
        m = int(input("Enter the module value (m): "))
        a = int(input("Enter the multiplier value (a), it must be ≤2: "))
        c = int(input("Enter the increase value (c): "))
        s = int(input("Enter the seed value (s), it must be ≤0: "))
        print ("\n")

        # Function
        def pseudorandomNumberGenerator(s, m, a, c, randomNumbers, numbersQuantity):
            randomNumbers[0] = s
            for i in range(1, numbersQuantity):
                randomNumbers[i] = ((randomNumbers[i - 1] * a) + c) % m
        
        # Output quantity
        numbersQuantity = 5
        randomNumbers = [0] * (numbersQuantity)
        pseudorandomNumberGenerator(s, m, a, c, randomNumbers, numbersQuantity)

        # Data print
        for i in randomNumbers:
            print(i, end = " ")

    else:
        print("\nERROR: Please type a valid option.")
