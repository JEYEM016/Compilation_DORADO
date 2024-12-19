import os
name = input ("Please Enter your name:  ")

#Starting
def get_started():
    os.system('cls')
    while True:
        print (f"Hi {name}, Welcome to DORADO's python tutorial!")
        user= input("Would you like to start program? Yes / No:  ")

        if user.lower() == "yes":
            menu()
        elif user.lower() == "no":
            print("Okay, Bye!")
            break

def goodbye():
    while True:
        os.system ('cls')
        print("Thank you for using the program, GOODBYE!")
        exit()

#HOME
def menu():
    while True:
        os.system('cls')
        print (f"Hi, {name} you may now explore the program.")
        print("----------------------------------------------------")
        print("                     -Main Menu-                    ")
        print("1. Printing in Python")
        print("2. Variables in Python")
        print("3. Operators")
        print("4. Conditional Statement")
        print("5. Looping statement")
        print("6. Functions")
        print("7. List")
        print("8. Exit")
        print()
        print("----------------------------------------------------")

        choice = input("How would you like to proceed?Pick a number:    ")
            
        if choice == "1":
            print_g()
        if choice == "2":
            Var_name()
        if choice == "3":
            operators()
        if choice == "4":
            con_statement()
        if choice == "5":
            loop_stat()
        if choice == "6":
            functions()
        if choice == "7":
            list()
        if choice == "8":
            goodbye()
            
#1.Printing menu
def print_g():
    os.system('cls')
    print("Welcome to Printing in Python")
    print()
    print("In Python, printing refers to displaying output on the screen using the print()function.\nIt’s used to show text, numbers, or other data during the execution of a program.")
    print()
    
    while True:
        print("--------------------------------------------------------")
        print("                 -Menu in Printing-                     ")
        print("1. Example of PRINTING")
        print("2. Printing with STRING and CONCATENATION  ")
        print("0. Back to MENU")
        print()
        print("--------------------------------------------------------")

        choice = input("Choose a number in Printing Menu that you like to learn:    ")

        if choice == "1":
            printing_P()

        if choice == "2":
            Strng_Conca()
        
        if choice == "0":
            return menu()
        

#Under Printing menu
def printing_P():

    os.system("cls")
    print ("INPUT:")
    print("print (\"USA\")")
    print("print (\"MISS U\")")
    print("print (\"Kangaroo\")")
    print()
    print("OUTPUT:")
    print("USA \nMISS U \nKangaroo")
    print()

    back = input("Type 0 to back:   ")
    if back == "0":
        print_g()
    else:
        print("Invalid input")
        return back


#Under printing Menu
def Strng_Conca():
    os.system('cls')
    print()
    print("""Strings are sequences of characters enclosed in quotes single ' or double " quotes.\nYou can store and manipulate text using strings.""")
    print()
    print("""INPUT:
          
name = input("What is your name? ")

# Manipulate the string
greeting = f"Hello,{name}! Welcome to Python."

# Output the result
print(greeting)""")
    
    print()
    print("""OUTPUT:
What is your name? Alice
Hello,Alice! Welcome to Python. 
          """)

    back = input("Type 0 to back:   ")
    if back == "0":
        print_g()
    else:
        print("Invalid input")
        return back
    
#2. Variables
def Var_name():
    while True:
        os.system('cls')
        print()
        print("Welcome to Variables in Python")
        print()
        print("""A variable is a name used to store data in a program. Variables act as "containers" \nthat hold values, which can be text, numbers, or other types of data. Once a variable \nis assigned a value, it can be reused or modified throughout the program.""")
        print()
        print("------------------------------------------------------")
        print("                   -Variables Menu-                   ")
        print()
        print("1. Feature of Variable ")
        print("2. Example of Variable")
        print("0. Back to MAIN MENU")
        print("------------------------------------------------------")

        choice = input("Choose a number you want to proceed:    ")

        if choice == "1":
            var_f()
        if choice == "2":
            var_e()
        if choice == "0":
            menu()

def var_f():
    os.system('cls')
    print()
    print("Feature of Variable")
    print("""Dynamic Typing: You don’t need to specify the variable type (e.g., int, float, string).
Reassignment: Variables can change their type during runtime by assigning a new value.
Case-Sensitive: Variable names are case-sensitive (name and Name are different variables).
""")
    print()
    back = input("Type 0 to back:   ")
    if back == "0":
        Var_name()
    else:
        print("Invalid input")
        return back

def var_e():
    os.system('cls')
    print()
    print("Example of Variable")
    print()
    print("Syntax : variable_name = value ")
    print("You cannot use a variable name starting with number")
    print("INPUT and OUTPUT")
    print("""Integer variable:
x = 10
print(x)  # Output: 10

String variable:
name = "John"
print(name)  # Output: John

Float variable:
pi = 3.14
print(pi)  # Output: 3.14

Boolean variable:
is_active = True
print(is_active)  # Output: True

          """)
    back = input("Type 0 to back:   ")
    if back == "0":
        Var_name()
    else:
        print("Invalid input")
        return back

#3.Operators
def operators():
    while True:
        os.system('cls')
        print()
        print("In Python, operators are special symbols or keywords that perform operations \non variables and values. They are used to manipulate data and perform calculations.")
        print()
        print("------------------------------------------------------")
        print("                   -Operators Menu-                   ")
        print("1. Types of Operators")
        print("2. Example Program using Operators")
        print("0. Back to MAIN MENU")
        print()
        print("------------------------------------------------------")

        choice = input("Choose a number you want to proceed:    ")

        if choice == "1":
            t_operators()
        if choice == "2":
            examp_operators()
        if choice == "0":
            menu()


def t_operators():
    while True:
        os.system('cls')
        print("Types of Operators in Python:")
        print()
        print("""Arithmetic 
Operator	  Description	             

+	          Addition	            
-	          Subtraction	            
*	          Multiplication	    
/	          Division	            
%	          Modulus (remainder)	    
**	          Exponentiation	    
//	          Floor Division	    
              
              """)
        print("""Comparison
Operator	Description	
              
==	        Equal to	
!=	        Not equal to	
>	        Greater than	
<	        Less than	
>=	        Greater than or equal to	
<=	        Less than or equal to
              
              """)
        print("""Logical
Operator       Description	
              
and	       True if both are true	
or	       True if one is true	
not	       Reverses the condition
      
      """)
        print("""Assignment
Operator    Description	
      
=           Assign	
+=	    Add and assign	
-=	    Subtract and assign	
*=	    Multiply and assign	
/=	    Divide and assign	
%=	    Modulus and assign	
**=	    Exponentiate and assign	
//=	    Floor divide and assign    
              
              """)


        back = input("Type 0 to back:   ")
        if back == "0":
            operators()
        else:
            print("Invalid input")
            return back
        
def examp_operators():
    while True:
        os.system('cls')
        print()
        print("""a = 10
b = 5

INPUT:
print("Arithmetic Operators:")
print("Addition:", a + b)       
print("Subtraction:", a - b)    
print("Multiplication:", a * b)
print("Division:", a / b)   
              
OUTPUT:
Arithmetic Operators:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

INPUT:         
print("Comparison Operators:")
print("Is a equal to b?", a == b) 
print("Is a greater than b?", a > b)
              
OUTPUT:
Comparison Operators:
Is a equal to b? False
Is a greater than b? True

INPUT:
print("Logical Operators:")
x = True
y = False

print("x AND y:", x and y) 
print("x OR y:", x or y)  
print("NOT x:", not x) 

OUTPUT:
Logical Operators:
x AND y: False
x OR y: True
NOT x: False

INPUT:              
print("Assignment Operators:")
c = 10
print("The value of c is", c )
c += 2
print("The value of c is", c )    
c -= 5
print("The value of c is now" ,c)     

OUTPUT:
Assignment Operators:
The value of c is 10
The value of c is 12
The value of c is now 7  
              
              """)
        back = input("Type 0 to back:   ")
        if back == "0":
            operators()
        else:
            print("Invalid input")
            return back
            
#4.CONDITIONAL STATEMENT
def con_statement():
    while True:
        os.system('cls')
        print("""A conditional statement in Python allows your program to make decisions \nand execute certain blocks of code based on whether a condition is true or false. \nIt's commonly used to control the flow of the program.""")
        print("------------------------------------------------------")
        print("           -Menu of CONDITIONAL STATEMENT-            ")
        print()
        print("1. Conditional Statement Example")
        print("2. Conditional Statement Example Program")
        print("0. Back to MENU")
        print()
        print("------------------------------------------------------")

        choice = input("Choose a number you want to proceed:   ")

        if choice == "1":
            con_explanation()
        if choice == "2":
            con_example()
        if choice == "0":
            return menu()
        
        
#Under 3
def con_explanation():
    os.system('cls')
    print()
    print("The most common conditional statements in Python are:    ")
    print()
    print("if statement - Used to execute code only if a condition is true.")
    print("if-else statement - Provides an alternative block of code if the condition is false.")
    print("if-elif-else statement - Allows you to check multiple conditions in sequence.")
    print("Nested if statements - You can place one if inside another to check for more specific conditions.")
    print()

    back = input("Type 0 to back:   ")
    if back == "0":
        con_statement()
    else:
        print("Invalid input")
    return back


def con_example():
    while True:
        os.system('cls')
        print()
        print("""INPUT:
age = int(input("Enter your age: "))

# Check eligibility using conditional statements
if age < 13:
    print("You are a child.")
    print("You can play in the kids' zone.")
elif 13 <= age < 18:
    print("You are a teenager.")
    print("You can participate in the teen program.")
elif 18 <= age < 21:
    print("You are an adult.")
    print("You can vote but cannot drink alcohol in some countries.")
else:
    print("You are a full adult.")
    print("You can vote and drink alcohol responsibly.")

# Closing statement
print("Thank you for checking your eligibility!")""")
    
        print("Example input: Enter age: 16")   
        print("OUTPUT:")
        print("""You are a teenager.
You can participate in the teen program.
Thank you for checking your eligibility!""")
        print()

        back = input("Type 0 to back:   ")
        if back == "0":
            con_statement()
        else:
            print("Invalid input")
        return back
    
#4
def loop_stat():
    
    while True:
        os.system('cls')
        print("""A loop statement in Python is used to repeatedly execute a block of code \nas long as a specified condition is met or for a fixed number of times. \nThis is useful for automating repetitive tasks.""")
        print("-------------------------------------------------------")
        print("               -Menu for LOOP STATEMENT-               ")
        print("1. Types of Loop Statements in Python ")
        print("2. Example program of Loop Statement")
        print("0. Back to MAIN  MENU")
        print()
        print("-------------------------------------------------------")

        choice = input("Enter a number you want to proceed:    ")

        if choice == "1":
            loop_types()
        if choice == "2":
            exam_loop()
        if choice == "0":
            menu()



def loop_types():
    while True:
        os.system('cls')
        print("for Loop - The for loop iterates over a sequence (e.g., list, tuple, string, range) \nand executes a block of code for each item in the sequence.")
        print ("Syntax - for item in sequence ")
        print("Example INPUT:")
        print ("""for num in range(5):  # Loops from 0 to 4
        print(num)""")
        print()
        print("OUTPUT:")
        print("""0
1
2
3
4
""")

        print("while Loop - The while loop executes a block of code as long as a given condition is True.")
        print ("Syntax: \nwhile condition: #code to execute ")
        print("Example INPUT:")
        print ("""count = 0
while count < 5:  # Loop runs until count is no longer less than 5
    print(count)
    count += 1  # Increment count to avoid infinite loop""")
        print()
        print("OUTPUT:")
        print("""0
1
2
3
4
""")
        print()
        back = input("Type 0 to back:   ")
        if back == "0":
            loop_stat()
        else:
            print("Invalid input")
            return back
        

def exam_loop():
    while True:
        os.system('cls')
        print()
        print("Example INPUT:")
        print("""# Get user input
    number = int(input("Enter a number to display its multiplication table: "))

# Using a for loop
    print("Multiplication Table using a for loop:")
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{number} x {i} = {number * i}")

# Using a while loop
    print("Multiplication Table using a while loop:")
    count = 1
    while count <= 10:  # Loop until count is greater than 10
        print(f"{number} x {count} = {number * count}")
        count += 1  # Increment the counter""")
    
        print("Example OUTPUT:")
        print("Enter a number to display its multiplication table: 5")
        print("""Multiplication Table using a for loop:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Multiplication Table using a while loop:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50""")
        print()

        back = input("Type 0 to back:   ")
        if back == "0":
            loop_stat()
        else:
            print("Invalid input")
            return back
#5
def functions():
    while True:
        os.system('cls')
        print()
        print("A function in Python is a block of reusable code that performs a specific task. \nFunctions help organize and simplify code by allowing you to write it once and \nuse it multiple times.")
        print()
        print("-------------------------------------------------------")
        print("                  -Function menu-                      ")
        print("1. Features of Function")
        print("2. Type and Example of Function")
        print("0. Back to MENU")
        print()
        print("-------------------------------------------------------")

        choice = input("Choose a number you want to proceed:    ")

        if choice == "1":
            f_function()
        if choice == "2":
            function_examp()
        if choice == "0":
            menu()

def f_function():
        os.system('cls')
        print("Feature of Function:")
        print()
        print("Reusability: Write a function once and call it multiple times.\nModularity: Break code into smaller, manageable pieces.\nMaintainability: Makes the code easier to debug and modify.\nPredefined or Custom: Python provides many built-in functions (e.g., print(), len()), and you can define your own custom functions.")
        print()
        back = input("Type 0 to back:   ")
        if back == "0":
            functions()
        else:
            print("Invalid input")
            return back

def function_examp():
    os.system('cls')
    print("Function:")
    print("1. Built-in Functions: These are provided by Python (e.g., print(), len(), input()).")
    print ("Example INPUT:")
    print("""print("Hello, World!")  # Prints a message
length = len("Python")  # Returns the length of the string
print(length)""")
    print("OUTPUT:")
    print("""Hello, World!
6""")
    print()
    print("2. User-Defined Functions: These are created by the programmer to perform specific tasks.")
    print ("Use the def keyword to define a function.")
    print("Example INPUT:")
    print()
    print("""def say_hello():
    print("Hello, World!")
          
say_hello()  # Call the function""")
    print()
    print("OUTPUT:")
    print("Hello, World!")
    print()
    back = input("Type 0 to back:   ")
    if back == "0":
        functions()
    else:
        print("Invalid input")
        return back

#6.List
def list():
    os.system('cls')
    print()
    print("A list in Python is a data structure that allows you to store multiple \nitems in a single variable. Lists are ordered, mutable (can be changed), \nand can hold items of different data types (e.g., integers, strings, floats, or even other lists).")
    print("---------------------------------------------------------")
    print("                     -List Menu-                         ")
    print("1. Features of List")
    print("2. Example of List")
    print("3. List operations")
    print("0. Back to MAIN MENU")
    print()
    print("---------------------------------------------------------")

    choice = input("Choose a number you want to proceed:")
    if choice == "1":
        f_list()
    if choice == "2":
        e_list()
    if choice == "3":
        o_list()
    if choice == "0":
        menu()
#Feature of list
def f_list():
    while True:
        os.system('cls')
        print("Features of List:")
        print()
        print("""Ordered: Items in a list maintain the order in which they are added.
Mutable: You can add, remove, or modify elements in a list.
Heterogeneous: A single list can contain items of different types.
Indexed: Each item has a specific position (starting at index 0""")
        print()
        back = input("Type 0 to back:   ")
        if back == "0":
            list()
        else:
            print("Invalid input")
            return back
#example of LIST    
def e_list():
    os.system('cls')
    print ("Example of List:")
    print()
    print("Example INPUT and OUTPUT:")
    print("You can access the list using their index")
    print("""fruits = ["apple", "banana", "cherry"]

# Access first item (index 0)
print(fruits[0])  # Output: apple

# Access last item using negative indexing
print(fruits[-1])  # Output: cherry
          """)


    back = input("Type 0 to back:   ")
    if back == "0":
        list()
    else:
        print("Invalid input")
        return back
    
#list Operations
def o_list():
    while True:
        os.system('cls')
        print()
        print("""Adding Items
-append(item): Adds an item to the end of the list.
-insert(index, item): Inserts an item at a specific index.
          
Removing Items
remove(item): Removes the first occurrence of the item.
pop(index): Removes the item at the specified index (or the last item if no index is specified).
clear(): Removes all items from the list.
""")

        print("Example INPUT and OUTPUT:")
        print("""fruits = ["apple", "banana"]
fruits.append("cherry")  # Adds "cherry" to the end
fruits.insert(1, "orange")  # Inserts "orange" at index 1
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']
          """)

        print ("The same with Removing items")

        back = input("Type 0 to back:   ")
        if back.lower() == "0":
            list()
        else:
            print("Invalid input")
            return back

get_started()