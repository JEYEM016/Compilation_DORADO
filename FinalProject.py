lives = 3
answer = eval(input("Guess the number between 1 to 100 :     "))
while lives > 3 :
    if answer == "58" :
        print ("You are such  good singer")
        break
    elif answer != "58" :
        lives == lives - 1
else:
    print ("You lose")