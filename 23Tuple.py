#----------------------------Intro ------------------
# tup = (1, 2, 3 ,4, 5, 6)
# print(type(tup))

# tup2 = (1)          # It is considered as integer 
# print(type(tup2))
# tup2 = (1, )        # It is considered as tuple 
# print(type(tup2))
#----------------------------------------------------

# tup3 = (1, 2, 3,  4, 5 ,6 )
# print(tup3[0])
# print(tup3[1])
# print(tup3[2])
# print(tup3[3])
# print(tup3[4])
# print(tup3[5])

# print("Length of tuple  :" , len(tup3))

# if 4 in tup3:
#     print(f"4 Present in tuple ")


# tup4 = tup3[1:4]
# print(tup4)



tu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tu1 = tu
tu2 = tu[1:6]

print(tu1)
print(tu2)
if 3 in tu:
    print ("Yes present")
else : 
    print("Not present")

print( "Length of the tupple is: " , len(tu))









