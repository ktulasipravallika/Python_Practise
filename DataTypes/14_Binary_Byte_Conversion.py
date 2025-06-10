name= input("Enter your name: ")
byte_code = name.encode()
print("Name:", name)
print("Byte Code: ", byte_code)

print("Type of Bytes code:", type(byte_code))

try:
    byte_code[0] = 'T'
except TypeError as e:
    print("Error:",e)


