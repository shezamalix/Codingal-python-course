import math

actual_cost = float(input("Enter the actual cost of the item:"))
sale_price = float(input("Enter the price you sold the item at:"))

if sale_price > actual_cost :
    print("You made a profit of")

elif sale_price == actual_cost :
    print("You made no profit or loss of")

else :
    print("You had a loss")

print("your profit or loss is equal to", math.fabs(sale_price - actual_cost))