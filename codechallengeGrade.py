Prelims = eval(input("Enter your Prelims Grade :  "))
Midterm = eval(input("Enter your Midterms Grade :  "))
Semifinals = eval(input("Enter your Semi-finals Grade :	 "))
Finals = eval(input("Enter your Finals Grade :	"))
Quiz = eval(input("Enter your Quiz :   "))
Project = eval(input("Enter your Project Grade :  "))

FG = (round (Prelims * 0.15) + (Midterm * 0.15)  +  (Semifinals * 0.15) + (Finals * 0.15) + (Quiz * 0.25) + (Project * 0.15))

print ("Your Final Grade is" , FG)
 
if FG >= 75 :
	print ("CONGARATULATION, You passed your course")
	print ("Enter to the next level!!")

else:
	print ("You failed, try again next time T^T")