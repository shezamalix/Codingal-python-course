class Employee:

    #Initializing
    def __init__(self):
        print("Employee created")

    #Calling destructor
    def __del__(self):
        print("Destructor called")

def Create_Obj():
    print("Making Object...")
    Obj = Employee()
    print("function end...")
    return Obj

print("Calling create_obj() function")
obj = Create_Obj()
print("Program End...")