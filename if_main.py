def welcome():
    print("Welcome!")

if __name__=="__main__":
    welcome() #function called in file which is to imported then it will print 2 times in other file


def day_(day):
    match day:
        case "a":
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("wednesday")
        case _:
            print ("enter valid number")

print(day_("as"))