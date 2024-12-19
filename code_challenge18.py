def factorial(number):
    """ This function is for calculating factorial, just put the number inside the parenthesis """
    fact = 1 
    for x in range (number, 0, -1):
        fact *= x
    return fact 

help(factorial)