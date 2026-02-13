# ZeroDivisionError = When you try to divide a number by zero.
# TypeError=  When you try to add a string to a integer 
# ValueError= When you typecast wrongly e.g int("pizza") cant convrt str into int

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception: # includes all kinds of exceptions
    print("Something went wrong!")
finally:
    print("Do some cleanup here")