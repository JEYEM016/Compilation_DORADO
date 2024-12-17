import os
def get_started():
    print ("Hi, Welcome to my Final project compilation")
    enter = input("Would you like to explore my final project? YES or NO     ")

    if enter.lower() == "yes":
        os.system('cls')
        name = input("Please enter your name:   ")
        print(f"Hi, {name} you are inside the system")

        while True:

            print("What code challange do you want to look?")
            print ()
            print ("Enter 1 - Codechallenge1")
            print ("Enter 2 - Codechallenge2")
            print ("Enter 3 - Codechallenge3")
            print ("Enter 4 - Codechallenge4")
            print ("Enter 5 - Codechallenge5")
            print ("Enter 6 - Codechallenge6")
            print ("Enter 7 - Codechallenge7")
            print ("Enter 8 - Codechallenge8")
            print ("Enter 9 - Codechallenge9")
            print ("Enter 10 - Codechallenge10")
            print ("Enter 11 - Codechallenge11")
            print ("Enter 12 - Codechallenge12")
            print ("Enter 13 - Codechallenge13")
            print ("Enter 14 - Codechallenge14")
            print ("Enter 15 - Codechallenge15")
            print ("Enter 16 - Codechallenge16")
            print ("Enter 17 - Codechallenge17")
            print ("Enter 18 - Codechallenge18")
            print ("Enter 19 - Codechallenge19")
            print ("Enter 20 - Codechallenge20")
            print()

            pili = input("Please enter the no. of the codechallenge you want to look:   ")

            if pili == "8":
                code8()
            elif pili == "9":
                code9()
            elif pili == "10":
                code10()
                break
                

def code8():
    os.system('cls')
    odd = 0
    even = 0
    sum = 0
    for numbs in range(1, 11):
        num = eval(input(f"Input #{numbs} :"))
        sum += num
        print (f"The sum of input number is {sum}")
        if numbs % 2 == 0:
            even += num
            print (f"The sum of even number is: {even} ")
        else:
            odd += num
            print (f"The sum of odd numbers is: {odd}")


def code9():
    os.system('cls')
    while True:
        check = input("DO you wnat to check the code challenge9? Yes or No  ")
        if check.lower() == "yes":

            for x in range(0, 9):
                for y in range(x):
                    print(" ", end=" ")
                for y in range(9 - x):
                    print("*", end=" ")
                print()
        else:
            print("Okay")
        print ("That's it!")

        return check

def code10():
    os.system('cls')
    
    while True:
        check = input("Do you want to check code challenge 10? Yes or No ")
        if check.lower() == "yes":
    
            for x in range(5, 0, -1):
                for y in range (1, x +1):
                    print (" ", end = " ")
                for z in range (5, x, -1):
                    print ("*", end =" ")
                for a in range (4, x, -1):
                    print ("*", end = " ")

                print ()

            for x in range (0, 5):
                for y in range (1, x +1):
                    print (" ", end=" ")
                for z in range (5, x, -1):
                    print ("*", end=" ")
                for a in range (4, x, -1):
                    print ("*", end=" ")

                print()
            
            seeg = input("Would you like to print it again? Yes or No   ")

            if seeg.lower() == "yes":
                continue
            elif seeg.lower() == "no":
                break
            else:
                print ("Invalid")
        

        print("That's it!")

    return check
    
get_started()