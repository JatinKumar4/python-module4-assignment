import math 
n=float(input("Enter the number"))
if n < 0:
    print("Error: Square root and logarithm are not defined for negative numbers.")
elif n == 0:
    print("Error: Logarithm is not defined for zero.")
sqr=math.sqrt(n)
loge=math.log(n)
sine=math.sin(n)

print(f"Square root of {n} is: {sqr}")
print(f"Natural logarithm of {n} is: {loge}")
print(f"Sine of {n} radians is: {sine}")