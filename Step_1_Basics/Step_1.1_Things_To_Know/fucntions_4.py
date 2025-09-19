# Functions with return values and parameterised

def minimum(num1,num2):
   return(min(int(num1),int(num2)))
def maximum(num1,num2):
   return(max(int(num1),int(num2)))

print(minimum(10,20))
print(minimum(20,30))
print(maximum(10,20))
print(maximum(20,30))

# Functions with multiple return values and parameterised

def min_max(num1,num2):
   return(min(int(num1),int(num2)),max(int(num1),int(num2)))

minimum_val,maximum_val=min_max(12123,124423)

print("Min_Value : ",minimum_val,"Min_Value : ", maximum_val)
