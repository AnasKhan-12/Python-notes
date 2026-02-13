# marks = [ 3, 4, 5, 6]
# print(marks)
# print(type(marks))

# marks.append(7)    # ----------It add 1 element in list
# for i in marks:
#    print(i)


# colors= ["Red", "Orange", "Pink", "Grapes", 1, 2, 3, 4, 5]
# print(colors[len(colors)-3])

# if "Orange" in colors : 
#    print(True)
# else : 
#    print(False)

# print(colors[1:9:2])

#------------------List Comprehension------------------------
lst =  [i*i for i in range(4)]
print(lst)
lst =  [i*i for i in range(10) if i%2 == 0]
print(lst)
