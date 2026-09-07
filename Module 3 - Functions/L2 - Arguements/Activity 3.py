# #Called a recusrive function call(call the same function inside the function)
# def hello():
#     print("Hello")
#     hello()  

# hello()  

def factorial(x):
    if x == 1 :
        return 1

    return x * factorial(x-1)

n = 5
print(factorial(n))
#answer should be 120

