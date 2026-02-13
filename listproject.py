foods=[]
prices=[]
total=0

while True:
    food= input("Enter the food you want (or press q to quit): ")
    
    if food.lower() == "q":
        break

    if food.isnumeric():
        print("Enter a valid food item, not a number!")
        continue

    else:
        try:
            price=float(input("Enter the price of food: "))
        except ValueError:
            print("enter a valid number")
        foods.append(food)
        prices.append(price)

print("-----YOUR CART------")

for items in foods:
    print(items)

for p in prices:
    total+=p
    print(f"YOUR TOTAL {total}")