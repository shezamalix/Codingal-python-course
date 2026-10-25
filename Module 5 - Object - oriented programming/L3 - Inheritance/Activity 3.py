#parent class
class bird:
    
    def __init__(self):
        print("Bird is ready")

    def whosisthis(self):
         print("Bird")

    def swim(self):
         print("swim faster")

#child class

class penguin(bird):
     def __init__(self):
          #call super() function to access the parent keyword properly
          super().__init__()
          print("Penguin is ready")

    def whoisthis(self):
        print("Penguin")

    def run(self):
     print("run faster")

#object creation
peggy = Penguin()
peggy = whoisthis()
peggy.swim()
peggy.run()
    

    
    