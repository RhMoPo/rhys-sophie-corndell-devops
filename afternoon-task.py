#!/usr/bin/env python3.9
def calculator():
    while True:
        # we want to prompt for the users input

        ##prompt for operation 
        operation = input("Enter an operation [+, -, x, /]: ")
        if operation not in ["+","-","x","/"]:
            print("No good - Enter an operation [+, -, x, /]: ")
            return
        
        ##prompt for the integers
        A = int(input("Enter an integer:"))

        B = int(input("Enter an integer:"))


        # carry out calc based on user input 
        if operation == "+":
            result = A + B
        elif operation == "-":
            result = A - B
        elif operation == "x":
            result = A * B
        elif operation == "/":
            result = 0 if B == 0 else A / B
        # output the result 


        print("result", result)

calculator()