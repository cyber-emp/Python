# Create a shopping cart program that will continuesly ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# at the end show the fodd items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quite:  ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the product {food}: R "))
        foods.append(food)
        prices.append(price)
        
print("------ YOUR CART ------")

for food in foods:
    print(food, end=  "  ")
    
for price in prices:
    total += price

print("\n")
print(f"Your total sandwhich: R {total}")

kyle = []

while True:
    kyle = input("is kyle gay? (yes/no): ")
    if kyle == "yes":
        print ("yes kyle is!")
    elif kyle == "no":
        print ("you fucking liar, taking the piss are you... Of course Kyle is gay")
        
for kyle in kyle:
    print(kyle, end=" ")