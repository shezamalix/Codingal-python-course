class Computer:

    def __init__(self):
        self.__maxprice == 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxprice(self,price):
        set.__maxprice = price

c = Computer()
c.sell()

#Change the pri e
c.__maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()