def greet_Someone():
    print("Hi , hoped your having a beautiful day.")


def greet_Person(name):
    print(f"Hi {name}, hoped your having a beautiful day.")

def Right_triangle():
    for x in range(1, 6):
        for y in range(1, x+1):
            print("*", end=" ")
        for z in range(6, x, -1):
            print(" ",end= " ")
        print()

def get_info(name, age):
    print(f"Hi {name}, with age {age} yrs old.")


def factorial(number):
    #factorial of 4 - 4 x 3 x 2 x 1 
    fact = 1 
    for x in range(number, 0, -1):
        fact *= x
    print(f"The factorial of {number} is {fact}")

tuloy = True

while tuloy:
    print("-------------------------------")
    print("WELCOME TO MY COMPILATION PROGRAM")

    print("Please select from the option BELOW:")
    print("1 - RIGHT TRIANGLE")
    print("2 - FACTORIAL")
    print("3 - GREET SOMEONE")
    print("4 - EXIT")

    pili = eval(input("Which program would you like to run (1,2,3,4) ----> "))

    if pili == 1:
        print("This program will show you a RIGHT TRIANGLE made from PYTHON")
        Right_triangle()
        continue
    elif pili == 2:
        print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
        num = eval(input("Enter a number:	 "))
        factorial(num)
        continue
    elif pili == 3:
        greet_Someone()
        continue
    elif pili == 4:
        print("Program Terminated")
        break
    else:
        print("YOU CHOOSE INVALID")
        print ("TRY AGAIN!")
        continue