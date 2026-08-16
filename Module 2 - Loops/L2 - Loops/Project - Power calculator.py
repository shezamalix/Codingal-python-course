base = int(input("Enter a base number :"))
power = int(input("Enter a power :"))

product = 1

for i in range (1,power+1):
    product = base * product
print(product)