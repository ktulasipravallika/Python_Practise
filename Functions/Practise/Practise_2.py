def f(y) :
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)


def g(y) :
    print(x)
    print(x+1)

x = 4
g(x)
print(x)


def h(y):
    global x # can be edited by usingglobal key word and then editing the varibale
    x +=1 # Cannot modify the global variable value directly with out global key word

x = 5
h(x)
print(x)

def l(x) :
    x = x +1
    print("in f(x) : x = ",x)
    return x
x = 3
z = l(x)
print("z in main", z)
print("x in main", x)

def z() :
    print("inside z")
    def k() :
        print("inside k")
    k()

z()


def b(x) :
    def c():
        x ='abc'
    x = x + 1
    print("in b(x), x is " , x)
    c()
    return x
x = 3
z = b(x)

def a(x) :
    def d(x):
        x = x+1
        print("in d(x), x is ", x)
    x = x+1
    print("in a(x), x is ", x)
    d(x)
    return x
x = 3
z= a(x)
print("in main x is ", x)
print("in main z is ", z)

def func_a():
    print("inside func_a")
def func_b(z):
    print("inside func_b")
    return z()

print(func_b(func_a))


def x() :
    def x(a, b):
        return a+b
    return x
val =f() (3,4)
print(val)