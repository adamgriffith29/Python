
import math
import sys
# Compute the real roots of the quadratic equation

# Ask the user for a, b, and c and get them
print("Solving the quadratic equation ax^2 + bx + c")
a, b, c = eval(input("Enter a, b, c "))

# Compute the "discriminant"
d = b*b - 4*a*c

# Get the sign of d
signd = 1

if (d < 0):
    signd = -1
else:
    signd = 1

if (signd > 0):
    x1 = -b + math.sqrt(d)/2*a
    x2 = -b - math.sqrt(d)/2*a
    # 1,5,6
    print("The roots are", x1, " ", x2)

else:
    # a=4, b=2, c=4
    print("The roots are complex")
    sys.exit(0)
