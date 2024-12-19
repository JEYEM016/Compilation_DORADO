#increment 

# for x in range(1, 10, -1):
#     for y in range (1, x, +1):
#         print (" ", end = " ")
#     for z in range (10, x, -1):
#         print ("*", end =" ")
#     for a in range (10, x, -1):
#         print ("*", end = " ")

#     print()


for x in range(0, 9):
    for y in range(x):
        print(" ", end=" ")
    for y in range(9 - x):
        print("*", end=" ")
    print()
 