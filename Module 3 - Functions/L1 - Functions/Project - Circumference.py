# create 2 functions, 1 for area and 1 for circumfurence
#take input of radius from user


def area(radius, pi):
    radius = int(input("Enter the radius of the circle : "))
    print(f"the area of the circle is {(radius ** 2) * pi}")

area("",3.14159)
