# Creating a Tuple

# Empty Tuple
T1 =()

# Homogeneous Tuple - same data type values
T2 =(1, 2, 3, 4, 5)

# Heterogeneous Tuple - different data type values
T3 =("Hello", 3.5, 6)

# 2D Tuple
T4 = (1, 2,(3,4))

# Single item Tuple - , should be included at the end
T4 = (6,)
print(type(T4))

# Creating tuple using tuple()
T5 = tuple("Hello")

# List in tuple

T6 = tuple([1, 2, 4, 5, 6])
print(T6)

# Tuples are immutable and inner elements cannot be edited , new elements cannot be added , existing elements cannot be deleted.
# T4[0] = 676
# T4[1] = 232
# del T4[0]


# Concatenation, multiplication, memebership operators(in , not in ) and loops can be performs
T7 = T4 + 3 * T6
for u in T7 :
    print(u)
print(10 in T7)

# Functions

print(len(T2))
print(min(T2))
print(max(T2))
print(sorted(T2))
print(sorted(T2, reverse = True))