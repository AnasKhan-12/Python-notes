import random

print("***************")
print("Welcom to Python Slot")
print("Symbols ❤️ 😊🤡")
print("***************")
print("Your balance: 300$ ")
balance=300
results=[]

def game():
    while True:
        try:
            bet=int(input ("Enter the amount to bet: "))
            if bet>balance:
                print("enter a valid bet")
            else:
                break
        except ValueError:
            print("Enter a valid number")


    symbols=['❤️ ', '😊','🤡']
    for i in range(3):
        results.append(random.choice(symbols))

    print(" | ".join(results))

    if results[0]== results[1] == results[2]:
        print(f"you won {bet*2}")
    else:
        print("You lose")

game()

while True:
    again= str(input("Do you want to play again?(y/n)"))
    if again == 'y':
        game()
    elif again == 'n':
        break
    elif again != 'y' or 'n':
        print("Enter a valid answer")
        # continue

# again= str(input("Do you want to play again?(y/n)"))
# if again == 'y' or 'n':
#     game()


