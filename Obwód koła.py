import math
r = float(input("Enter the radius of the circle: "))
PI = math.pi
area = PI * r**2
circumference = 2 * PI * r
print(f"For a circle with radius {r}:")
print(f"Circumference = {circumference:.2f}")
print(f"Area = {area:.2f}")