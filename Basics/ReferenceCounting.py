import sys

a = 25
b = a
c = b

print(id(a))
print(id(b))
print(id(c))

# To know how many variables are pointing to a particular reference (here it is reference "a")
ref_count = sys.getrefcount(a) - 1
print("Reference count of 'a':", ref_count)