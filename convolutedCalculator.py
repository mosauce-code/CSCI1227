# function to add two numbers
def add(x, y):
   return x + y

# function to subtract two numbers
def subtract(x, y):
   return x - y

# function to multiply two numbers
def multiply(x, y):
   return x * y

# function to divide two numbers
def divide(x, y):
   return x / y

# function to calculate the logarithm of a number
def log(x):
   return (len(str(x))-1) + (x/10**(len(str(x))-1)-1)*10

# function to convert degrees to radians
def to_radians(degrees):
    return degrees * (180/3.14)

# function to calculate the sine of an angle
def sin(x):
   x = to_radians(x)
   result = 0
   for n in range(10):
       result += ((-1) ** n) * (x ** (2*n + 1)) / factorial(2*n + 1)
   return result

# function to calculate the cosine of an angle
def cos(x):
   x = to_radians(x)
   result = 0
   for n in range(10):
       result += ((-1) ** n) * (x ** (2*n)) / factorial(2*n)
   return result

# function to calculate the tangent of an angle
def tan(x):
   return sin(x) / cos(x)

# function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("select an operation -\n" \
        "1. add\n" \
        "2. subtract\n" \
        "3. multiply\n" \
        "4. divide\n" \
        "5. log\n" \
        "6. sin\n" \
        "7. cos\n" \
        "8. tan\n")

# Take input from the user
choice = input("Enter choice (1/2/3/4/5/6/7/8):")

if choice == '1':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   num = float(input("Enter a number: "))
   print("log(",num,") =", log(num))

elif choice == '6':
   angle = float(input("Enter an angle in degrees: "))
   print("sin(",angle,") =", sin(angle))

elif choice == '7':
   angle = float(input("Enter an angle in degrees: "))
   print("cos(",angle,") =",)



'''
This *other *program calculates two numbers and has a selection for arithmetic operators.


a = int(input("Enter the first number:  "))
b = int(input("Enter the second number:   "))
c = (input("Enter the operator (+) (/) (-) (*) (pow):   "))

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "/":
    print(a/b)
elif c == "*":
    print(a*b)
elif c == "pow":
    print(pow(a , b))
else:
    print("Wrong command.")
'''