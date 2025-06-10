personDetails = {
    "name":"Tulasi",
    "age":"29",
    "city":"Vijayawada"
}

print(personDetails)

print("Name is :",personDetails["name"])
print("Age is :",personDetails["age"])
print("City is :",personDetails["city"])

personDetails["education"] = "MS"
print("Education is :",personDetails["education"])

personDetails["age"]="28"
print("Age is :",personDetails["age"])

del personDetails["age"]
print(personDetails)