def calculate_discounted_price(selling_price, discount_perc):
    #subtact percentage from 100
    #divide by 100
    #multiply by selling price
    price = ((100 - discount_perc) / 100) * selling_price
    return price 

#function always returns to where you called it

selling_price = float(input("Enter the selling price of the product : "))
discount_perc = float(input("Enter the sale discount percentage : "))
new_price = calculate_discounted_price(selling_price, discount_perc)
print(f"The price after a discount is {new_price} riyals")

# DOCSTRING - DOCUMENTATION STRING
# A comment that describes what the function does

print(calculate_discounted_price . __doc__)



# Default Arguments
def show_hobby(hobby = "gaming"):
    print(f"I like {hobby}")

show_hobby("swimming")
           