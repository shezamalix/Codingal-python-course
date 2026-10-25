class dad:
    def __init__(self,eyes,aggresive):
        self.eyes = eyes
        self.aggresive = aggresive

    def display(self):
        print("your eye colour is", self.eyes)
        print("you are aggresive", self.aggresive)

#child class
class son(dad):

    def __init__(self,name,age,eyes, aggresive):
        self.name = name
        self.age = age

        #invoking the __init__ of parent class to access it's attributes
        super().__init__(eyes,aggresive)

#object creation
obj = son("Penguin", 8, "blue", True)

#calling method display
obj.display()