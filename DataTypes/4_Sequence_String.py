string1= input("Enter Any String: ")

print("The length of the string is: ", len(string1))
print("Upper Case : ", string1.upper())
print("Lower Case: ", string1.lower())
print("String in reverse: ", string1[::-1])

reverseString = ""
for char in string1:
    reverseString= char+reverseString
print("String in reverse: ", reverseString)