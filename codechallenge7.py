name = input("Please enter your name:   ")
grocery = input("Did you purchase a grocery today (yes/no):    ")
if grocery == "yes":
    disc = 4000
    purchse = input("What did you purchase:    ")
    Pprice = eval(input("Item price:  ")) 
    age = eval(input("Your age please:   "))

    DisAmount = Pprice * 0.038 
    DisAmount2  = Pprice - DisAmount 
    taxamount =   Pprice * 0.123
    #Senior Discount
    if age >= 60 and age <= 150:
        print ("Your Total Bill with Senior Discount is:    " , DisAmount2 + taxamount ) 

        payment = eval(input("Payment :    "))
        change = (payment - (DisAmount2 + taxamount))
        print (f"Your change is {change} ")

    #4000pesos Up Shopping Discount
    elif Pprice >= disc: 
            
            print ("You purchase more than 4000, you have guaranteed 3.8% discount")
            print ("Your Total Bill with 12.3% tax is " , (0.038 * Pprice) + Pprice)
            payment = eval(input ("Payment :    "))
            change = (payment - ((0.038 * Pprice) + Pprice))
            print (f"Your change is {change} ")
    #No discount        
    else:
            print ("Your Total Bill with 12.3% tax is" , (0.123 * Pprice) + Pprice  )
            payment = eval(input ("Payment :    "))
            change = (payment - ((0.123 * Pprice) + Pprice))
            print (f"Your change is {change} " )


else:   
    print("Thank you for coming")