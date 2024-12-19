#sum of all given numbers are added until the user input 0
ToRepeat = True
sum = 0

while ToRepeat == True:
    num =eval(input("Enter a number: "))
    if num == 0:
        print("The Loop Terminated!")
        break
        Repeat= False
    
    else:
        sum += num
        print(f"The sum of all numbers are {sum}")
        continue