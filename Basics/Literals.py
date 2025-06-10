a = 0b1010 # Binary format
b = 100 #Decimal Format
c = 0o310 # Octal Format
d = 0x12c # Hexa decimal Format

float_1 = 10.4;
float_2 = 1.5e2;
float_3 = 1.5e-3;

# Complex Literal
x = 3.14j;

print(a, b, c, d);
print(float_1, float_2, float_3);
print(x, x.imag , x.real);

# String Literals

string1 ="1.) Hi this is Python"
string2 ='2.) Hi this is Python'
char1 = "c"
char2 = 'c'
multilineString = """This is a multiline string used to display multiple lines of data."""
unicode= u"\U0001f600"
raw_str = r"raw \n string"

print(string1)
print(string2)
print(char1)
print(char2)
print(multilineString)
print(unicode)
print(raw_str)


#Boolean Literal 

a = True + 5 # Takes True as 1 and False as 0 here
b = False + 10

print("a" , a)
print("b", b)

# Special Literal 

a = None
print(a);
