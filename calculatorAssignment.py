
# c = input("Please enter temp in celsius: ")
# result = 1.8*int(c)+32

# print(f"Temp in Feh is {result}")

# Dollar = input("Please enter an amount in Dollar: ")
# naira =float(Dollar) *1000
# print(f"Naira value of {Dollar} dollar is {naira}")
def Calculator():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("please enter a second number: "))

    operator = input("Please enter an operator, e.g +, -,*,/: ")

    #subtraction
    if operator == '-':
        print(num1-num2)

    #addition
    elif operator == '+':
        print(num1+num2)

    #division
    elif operator == '/':
        if num2 == 0:
            print('Division by zero error')
        else:
            print(num1/num2)
        
    
    #multiplication
    elif operator == '*':
        print(num1 * num2)
    elif operator == '^':
        print(num1 ** num2)
    elif operator == '%':
        print(num1 % num2)
    elif operator == '//':
        print(num1//num2)




    else:
        print("Sorry you probably entered an invalid operator, please try again")

#Calculator()



