#define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':90,
}

#Greetings
print("Welcome to our Restaurant")
print("Pizza: 40tk\nPasta: 50tk\nBurger: 60tk\nSalad: 70tk\nCoffee: 90tk\n")

order_total = 0

item_1 = input("Enter the name of the item: ")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item {item_1} has been ordered")
else:
    print(f"Ordered item {item_1} is not available")

another_order = input("Do you want to order anything else? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of your second order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of your order is {order_total}")
