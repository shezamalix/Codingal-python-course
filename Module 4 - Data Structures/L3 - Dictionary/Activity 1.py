currencies = {
    "Qatar" : "Qatari Riyal",
    "USA" : "US Dollar",
    "Saudia" : "Saudi Riyal",
    "France" : "Euro"
}

print(currencies["France"])

currencies["Japan"] = "Yen" #other way to assign values,adds it to the dictionary

print(currencies)

print(len(currencies))

#print(currencies["UAE"])

print(currencies.get("UAE","Country not found")) #only for dictionaries

country = input("Enter a country: ")
print(f"The currency of {country} is {currencies.get(country,'Not found')}")