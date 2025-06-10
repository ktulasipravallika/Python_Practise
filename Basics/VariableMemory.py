# The memory where variable is stored

a = 8
print(hex(id(a)))
print(hex(id(8)))
print(id(a))
print(id(8))

# Aliasing

a = 5
b = a
c = b

# The addresses remains same, here the variables a, b, c will be pointed to the same address

print(id(a))
print(id(b))
print(id(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

# Even if a is deleted , b and c will still be pointed to the memory address of 5.

del(a)
print(b)

# Even when value of a is changed, b and c contains value 5.

a = 6;
print(a)
print(b)
print(c)

L = [1, 2, 3, 4, 5]

print(id(1))
print(id(2))
print(id(3))
print(id(4))
print(id(5))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(L[3]))
print(id(L[4]))

L[4] = 3

print(id(L[4]))


