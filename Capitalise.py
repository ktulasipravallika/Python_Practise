sample = "how are you ?"

print(sample.split())
L = []
for i in sample.split() :
    print(i.capitalize())
    L.append(i.capitalize())

print(L)    
print(" ".join(L))    


email = "tulasipravalliak@gmail.com"
print(email[ :email.find('@')])