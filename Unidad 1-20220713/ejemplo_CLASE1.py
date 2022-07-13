# VARIABLES
x = 2
y = "hola"

print("\nVARIABLES-------------")
print(type(y))

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

_name = "Pedro"
Age = 16
age = 17
print("\nName Rules-------------")
print(age)

# PYTHON DATA TYPES

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

print("\nDATA TYPES-------------")
x = [1,2,3]
print(type(x))

y = {"name": "Daniel", "Edad": 18}
print(type(y))


print("\nCASTING-------------")
d = 5
g = "1"
print(d + int(g))

print("\nAssignment Operators-------------")
# =	    x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3
x=3
x*=1
print(x)

print("\nComparison Operators-------------")
# ==	Equal	                x == y	
# !=	Not equal	            x != y	
# >	    Greater than	        x > y	
# <	    Less than	            x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	    x <= y

print("\nLogical Operators-------------")
# and 	Returns True if both statements are true	        x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	    x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

print((1==1) and (1>3)) #false

print("\nIdentity Operators-------------")
# is 	    Returns True if both variables are the same object	            x is y	
# is not	Returns True if both variables are not the same object	        x is not y
print(1 is 1) #true
print(1 is not 2) #true

print("\nMembership Operators-------------")
# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
print(1 in [2,3,4]) #false
print(2 not in [3,4,5]) #true


print("\nIf ... Else-------------")

if (1 == 1):
    print("Si es igual")
else:
    print("no es igual")
    

x = [1,2,3]
y= [4,5,6]

if (4 in x):
    print("4 esta en x")
elif (4 in y):
    print("4 esta en y")
else:
    print("4 no esta en ningun lado")
    
print("1 es igual a 1") if 1==1 else print("no es igual")

print("\nFor loops-------------")

colors = ["red", "black", "yellow"]
for x in colors:
    print(x)
    
x = "hola"
for y in x:
    print(y)
    
colors = ["red", "black", "yellow"]
for x in colors:
    print(x)
    if x == "black":
        break #continue
    
print("\nWhile loops-------------")
i = 0

while i<5:
    print(i)
    i += 1
else:
    print("i llego al final")
    
print("\nFunctions-------------")

def sumar(x,y):
    return x + y

print(sumar(2,4))

def decirHola():
    print("hola")

decirHola()
    
