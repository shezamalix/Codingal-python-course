try:
    age = int(input("Enter the age:"))

    if(age<18):
        raise ValueError #way to delibrately pause an expception

    else:
        print("the age is valid")

except ValueError:
    print("The age is not valid")