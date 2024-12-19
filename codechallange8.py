#make for loop 

# Time to time update
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

#One time good time

# odd = 0
# even = 0
# sum = 0

# for numbs in range(1, 11):
#     num = eval(input(f"Input #{numbs} :"))
#     sum += num

#     if numbs % 2 == 0:
#         even += num

#     else:
#         odd += num

# print (f"The sum of all the numbers given is {sum}")
# print (f"The sum of even number is {even} ")
# print (f"The sum of odd numbers is {odd}")

# balance = 0 
# import os 
# def get_started():
#     global balance 
#     print("Hi!, Welcome to our Bank.")
#     user = input("Would you like to create a bank account with us? Y / N: ")

#     if user.lower() == "y":
#         name = input ("Please enter your name:  ")
#         os.system('cls')
#         print (f"Hi {name}, your bank accout is succesfully created.")
#         os.system('cls')

