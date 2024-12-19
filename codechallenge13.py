number = True
sum = 0

while number == True:
    num = eval(input("Enter a numbers:  "))
    sum += num 

    if num == 0:
        print(f"The sum of all numbers entered is {sum}")
        break
