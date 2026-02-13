# import if_main

# if_main.welcome()


# def calculateprice(price,discount=0,tax=0.05): #price is positional argument and discount,tax are Default argument
#     x =(price-discount)*(tax)
#     y=price+x
#     return y

# print(calculateprice(400,0,0.1))

def phone(country,first,last):
    return f"{country}-{first}{last}"

print(phone(country="+92",first=988,last=4535)) #keyword arguments



#-------Args and kwargs

def add(*num): #* unpacking operator
    total=0
    for i in num:
        total+=i
    return total

print(add(9,9,8))

#------

def name(*args):
    for arg in args:
        print(arg, end=' ')

name("Mr","Spongebob","squarepants")

#-----

def items(**kwarrgs):
    for key in kwarrgs.keys():
        print(key)

items(price="67",age="22",name="anas")

# for i in range(7,15):
#     print (i,end=' ')