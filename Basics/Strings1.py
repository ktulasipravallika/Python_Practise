# Creating Strings

# Single Quotes
c = 'Hello World'

# Double Quotes
d = "Hello World"

print(c)
print(d)

#Use of mix Quotes
a = "It's rainig outside today"
print(a)

# Multi Line Strings
b = '''Hello..'''
e = """World"""
print(b)
print(e)

# Using str()
f = str("Hello")
print(f)

#Positive Indexing
print(f[0])

#Negative Indexing
print(f[-1])

#Slicing
c = "Hello World"
print(c[0:4])# 4 not included -> 0-3 will be printed 

print(c[2:])# prints letters from 2 to end

print(c[:5]) # prints letters till 4

print(c[:]) # prints the whole word

print(c[0:8:3]) # prints the letters from 0 to 7 and skips 3 letters between

print(c[-5 : -1 : 2]) # prints using negative indexing

print(c[::-1]) # prints the words in reverse order

print(c[-1 : -5 : -1])