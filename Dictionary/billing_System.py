""" Simulate a billing scenario in a store with two dictionaries
    'stock' and 'price'. 'Stock' contains the items in the store with count.
    'Price' has the price of each item.
    The items that are available in the stock should be displayed to the user.
    User can buy any set of items from the stock.
    After purchase total bill of all items bought should be
    displayed with remaining stock items."""

num = int(input("\nEnter no.of items : "))
stock = {}
price = {}
for i in range(num):
    item = input("\nEnter the item : ")
    count = int(input("Enter the item count : "))
    rate = int(input("Enter the item price : "))
    stock[item] = count
    price[item] = rate
print("\n",stock)
total_Amount = 0
while(True):
    purchase = input("\nEnter the Item to be purchased : ")
    if purchase == "":
        break
    if purchase in stock:
        if stock[purchase] <= 0:
            print("Item out of Stock.")
        else:
            stock[purchase] -= 1
            total_Amount += price[purchase]
    else:
        print("Item not present.")

print("\nTotal Bill : ",total_Amount)

    
