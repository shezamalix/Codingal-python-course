# Class creation
class myClass:

    # private variable
    __privateVar = 27;

    #private method
    def __privmeth(self):
        print("I'm inside class myClass")

    # Function toprint value of private variable
    def hello(Self):
        print("Private variable value: ", myClass.__privateVar)

# Object creation method call
foo = myClass()
foo.hello()
