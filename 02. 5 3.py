###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
vol=a*b*c

x=(a*b)*2
y=(c*b)*2
z=(a*c)*2

sur=x+y+z
print(f"Volume is {vol}")
print(f"Surface is {sur}")