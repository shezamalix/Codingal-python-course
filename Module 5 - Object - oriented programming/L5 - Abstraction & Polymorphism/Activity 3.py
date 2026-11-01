#Class 1
class India():
    def capital(self):
        print("New Delhi is the capitala of India.")

    def language(self):
        print("Hindi is the most spoekn in India")

    def type(self):
        print("India is a developing country")

#Class 2
class USA():
    def capital(self):
        print("Wahsington, D.C. is the capital of USA.")

    def language(self):
        print("English is the most spoekn in USA")

    def type(self):
        print("USA is a developed country")

#Object creation
obj_ind = India()
obj_usa = USA()

#common interferance
for country in (obj_ind,obj_usa)
    country.capital()
    country.language()

