import sys
sys.path.append(' ')  # Adding the parent directory to the Python path

from EvenOrOdd import EvenOrOdd
from Power import Power 

for i in range(1, 100):
    print(i, EvenOrOdd.is_even(i))
    # You can use other imported functions here as needed

# To access the docstring of is_even:
print(EvenOrOdd.is_even.__doc__)


print("The power is ",Power.power(2, 3))
print("The power is ",Power.power(3))
print("The power is ",Power.power(b = 2 , a = 3))




