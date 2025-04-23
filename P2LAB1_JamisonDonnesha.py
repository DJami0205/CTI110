#Donnesha Jamison
#4/09/2025
#P2LAB1
import math
#Get Radius User.

radius = float(input("Enter the radius:") )

#calculate circum, diameter, area
cir= 2 * math.pi * radius
diam = 2 * radius
area= math.pi*(radius*radius)

#Display results

print(f"The diameter of the circle is {diam: .1f}")
print(f"The circumference of the circle is {cir: .2f}")
print(f"The area of the circle is {area: .3f}")
