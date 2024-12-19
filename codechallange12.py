for x in range (6, 1, -1):
    for y in range(1, x + 1):
        print(" ", end=" ")
    for z in range(6, x, -1): 
        print ("*", end=" ")
    for a in range(6, x, -1):
        print ("*", end=" ")

    print ()

for x in range (0, 4):
    for y in range (0, 2):
        print ("  ", end="   ")
    for z in range (0, 2):
        print ("*",end=" ")

    print ()

# for x in range (6, 1, -1):
#     for y in range(0, x -2):
#         print(" ", end=" ")
#     for z in range(6, x, -1): 
#         print ("*", end=" ")
#     for a in range(6, x, -1):
#         print ("*", end=" ")

#     print ()

# for x in range (4):
#     for y in range (2):
#         print ("  ", end=" ")
#     for z in range (2):
#         print ("*",end=" ")

#     print ()
