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
        div = 11
        arr = list(map(lambda x: x % div, arr))
        finalArr = []
        print(finalArr)

    # Second option || Pseudorandom number generator
    if option == "2":
        m = int(input("Enter the module value (m): "))
        a = int(input("Enter the multiplier value (a), it must be ≤2: "))
        c = int(input("Enter the increase value (c): "))
        s = int(input("Enter the seed value (s), it must be ≤0: "))
        print ("\n")
        def pseudorandomNumberGenerator(s, m, a, c, randomNums, numberOfRandoms):
            randomNums[0] = s
            numberOfRandoms = 5
            randomNums = [0] * (numberOfRandoms)
            for i in range(1, numberOfRandoms):
                randomNums[i] = ((randomNums[i - 1] * a) + c) % m
                pseudorandomNumberGenerator(s, m, a, c, randomNums, numberOfRandoms)
            for i in randomNums:
		        print(i, end = " ")

else:
    print("\nERROR: Please type a valid option.")
