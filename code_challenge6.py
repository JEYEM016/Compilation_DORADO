name = input("Enter your name:  ")
age = eval(input("Enter your age:   "))

if age >= 1 and age <= 8:
    print ("Toddler")

elif age >= 9 and age <= 18:
    print ("Pre-teen")

elif age >= 15 and age <= 18:
    print ("Teenanger")

elif age >= 19 and age <=27:
    print ("Early Adulthood")

elif age >= 28 and age <= 44:
    print ("Middle Age")

elif age >= 45 and age <= 59:
    print ("Post Adulthood")

elif age >= 60 and age <= 150:
    print ("Senior")

else:
    print ("Immortal?")