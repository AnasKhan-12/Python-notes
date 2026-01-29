#Decorator : A function that extends the behaviour of another function
# w/o modifying the base function. pass the base function as an argument to the decorator


def add_sprinkles(x):
    def wrapper_function():
        print("You added sprinkles")
        x()
    return wrapper_function


# @add_sprinkles # this line will take the function below as 'func' and pass it as argument to add_sprinkle
def get_icecream():
    print(f"Here is your  ice cream")
# get_icecream()

get_icecream = add_sprinkles(get_icecream) # add_sprinkle ka output yani wrapper get_ice cream ma agya
get_icecream()

# to ab ap jab basically get_icecream ko bulaogy t wrapper call hga

# def abc(van):  # this proves that wrapper (becuase it is returned) gets stored in get_icecream
#     print( van)
# c=abc
# c("i")