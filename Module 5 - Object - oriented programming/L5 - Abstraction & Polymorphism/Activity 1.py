#import necessary modules
from abc import ABC, abstractmethod

#create base class
class Absclass(ABC):

    # Function to print a value
    def print(Self,x):
        print("Passed value: ",x)

    #abstract method
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

#create sub class
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)