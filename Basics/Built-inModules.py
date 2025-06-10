import math
import random
import time
import os

print(math.factorial(2));
print(math.ceil(2.2342));
print(math.exp(2));
print(math.sqrt(22));
print(math.pow(1000,3));


print(random.randint(1,100));

a = [1, 2, 4, 5, 7, 8 ]
random.shuffle(a);
print(a);

print(time.time());
print(time.ctime());

print("Hello...")
time.sleep(10)
print("World")

print(os.getcwd())
os.listdir