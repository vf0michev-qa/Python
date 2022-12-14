# Homework 1 - Part 1 - 08.12.22
print("Homework 1 - 08.12.22")
print()

# Initialization of variables of different types
var1 = 'aqua'  # string variable initialization
var2 = 45  # integer variable initialization
var3 = 45.1  # float variable initialization
var4 = b'\x00\x00\x00'  # bytes variable initialization
var5 = [1, 2, 3]  # list variable initialization
var6 = ('red', 'blue', 'green')  # tuple variable initialization
var7 = {'black', 'blue', 'white'}  # set variable initialization
var8 = frozenset({2, 3, 9, 5})  # frozen set variable initialization
var9 = {'color': 'red', 'model': 'VC6', 'dimensions': '30x50'}  # dict variable initialization

# Output to the console all the above initialized variables with showing of their data type
print("Output to the console of all initialized variables of different types:")
print("var1 = ", var1, ", variable type is ", type(var1), sep="")
print("var2 = ", var2, ", variable type is ", type(var2), sep="")
print("var3 = ", var3, ", variable type is ", type(var3), sep="")
print("var4 = ", var4, ", variable type is ", type(var4), sep="")
print("var5 = ", var5, ", variable type is ", type(var5), sep="")
print("var6 = ", var6, ", variable type is ", type(var6), sep="")
print("var7 = ", var7, ", variable type is ", type(var7), sep="")
print("var8 = ", var8, ", variable type is ", type(var8), sep="")
print("var9 = ", var9, ", variable type is ", type(var9), sep="")
print()

# Initialization of 2 string variables, variables concatenation and output to the console
A = 'My name is '
B = 'Viktor'
C = A + B
print("Output result after initialization and concatenation of 2 string variables:")
print("var A is ", "'", A, "', ", "var B is ", "'", B, "'", sep="")
print("A + B = ", "'", C, "'", sep="")
print()

# Output of string and integer variables on the same line using comma ','
v1 = 'I am'
v2 = 30
v3 = 'years old'
print("Output result of string and integer variables on the same line using comma ',':")
print(v1, v2, v3, sep=" ")
print()

# Output of string and integer variables on the same line using plus '+'
v_1 = 'He is'
v_2 = 35
v_3 = 'years old'
v_sum = v_1 + ' ' + str(v_2) + ' ' + v_3
print("Output result of string and integer variables on the same line using plus '+':")
print(v_sum, sep=" ")