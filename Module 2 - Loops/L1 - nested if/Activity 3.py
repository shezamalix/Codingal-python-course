print("1.Pasta\n2.pizza")
pasta_pizza = input("Do you prefer pasta or pizza? ").lower()

if pasta_pizza == "pasta" or pasta_pizza == "1":
    print("1.Alfredo\n2.Arrabatia")
    pasta_flavor = input("What flavor would you prefer? ").lower()
    if pasta_flavor == "Alfredo" or pasta_flavor == "1" :
        print("Your alfredo pasta is on the way")
    else:
        print("Your arrabatia pasta is on the way")

elif pasta_pizza == "pizza" or pasta_pizza == "2":
    print("1.Ranch\n2.Cheese")
    pizza_flavor = input("What flavor would you prefer? ").lower()
    if pizza_flavor == "Ranch" or pizza_flavor == "1" :
        print("Your ranch pizza is on the way")
    else:
        print("Your cheese pizza is on the way")
    
