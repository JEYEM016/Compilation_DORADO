balance = 0 
import os 
#Creating bank account
def get_started():
    global balance 
    print ("Hi!, Welcome to our Bank.")
    user = input("Would you like to create a bank account with us? Yes or No  ")

    if user.lower() == "yes":
        os.system('cls')
        name = input ("Please enter your name:  ")
        print (f"Hi {name}, your bank account is succesfully created.")
    
        while True:
            print ("How would you like to proceed?")
            print ("------------------------------")
            print ()
            print ("1 - Deposit")
            print ("2 - Withdraw")
            print ("3 - Balance")
            print ("4 - Exit")
            print ()
            print ("------------------------------")

            pili = input("Which program would you like to do:    ")

            if pili == "1":
                deposit()

            elif pili == "2":
                withdraw()

            elif pili == "3":
                balnc()

            elif pili == "4":
                print ("You are now logout, Thank You!")
                break

    else:
        print ("Thank you for trusting us")
# to deposit
def deposit():
    global balance 
    os.system("cls")
    denomination()
    while True:
        depos = input("Enter the amount you want to deposit:   ")
        if depos.isdigit():
            depos = int(depos)
            os.system('cls')
            balance += depos
            print ("Your money is successfully deposited")
        
            d_again = input("Would you like to deposit again? Yes or No:     ")

            if d_again.lower() == "yes":
                continue
            elif d_again.lower() == "no":
                print ("Thank you")
                break
            else:
                print("Invalid")
                break
    return depos

def denomination():
    print("-----------------------------------------------")
    print("The Philippine Currency Denominations : ")
    print()
    print("1000  ----> 0")
    print("500   --->  0")
    print("200   --->  0")
    print("100   --->  0")
    print("50    -->   0")
    print("20    -->   0")
    print("10    -->   0")
    print("5     ->    0")
    print("1     ->    0")
    print()
    print("------------------------------------------------")

#withdraw your money
def withdraw():
    global balance
    os.system('cls')
    while True:
        print (f"Your current balance is {balance}")
        withd = input("Enter the amount you want to withdraw:  ")
        if withd.isdigit():
            os.system('cls')
            withd = int(withd)
            balance -= withd
            print ("You successfully withdraw")
            print(f"Your balance is now: {balance}")

            withd_again = input("Would you like to withdraw again? Yes or No:   ")

            if withd_again.lower() =="yes":
                continue 
            elif withd_again.lower() =="no":
                break
            else:
                print ("Invalid")
                break
    return withd
#To Check Your current balance
def balnc():
    global balance 
    os.system('cls')
    while True:
        check = input("Do you want to check your current balance? Yes / No:   ")
        if check.lower() == "yes":
            print (f"Your current balance is {balance} ")
            break
        elif check.lower() == "no":
            print ("Okay")
            break
    return check

get_started()