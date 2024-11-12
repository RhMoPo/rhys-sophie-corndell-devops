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

def calculator2(operation, A, B):
    # we want to prompt for the users input
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


    return result
#calculator()

#open txt file
f = open('step_2.txt')
lines = f.read().splitlines()
total = 0
for i in lines:
    line = i.split()
    total += calculator2(line[1], int(line[2]), int(line[3]))
print(total)