takbo = True
nt = 0
while takbo == True:
	int = input("Do you wish to add more triangles? (yes/no) --->    ")

	if int.lower() == "no":
			print("LOOP HAS BEEN STOPPED")
			break
			takbo = False

	elif int.lower() == "yes":
		nt += 1
		for x in range(1,6):
			for z in range(1, nt + 1):
				for y in range(1, x+1):
						print("*", end= " ")
				for a in range(6, x, -1):
						print(" ",end=" ")
				print(end=" ")
			print()
		continue
	else:
		print("Your Input is not accepted")
		print("Please Enter yes or no only")