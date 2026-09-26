#37. The surface of the cylinder is 149 cm². 
# The cylinder height is 6 cm. What is the diameter of this cylinder?
import math
csa=149
height=6

radius=csa/(2*3.14*height)
diameter=2*radius
print(f"diameter in case of curved surafce:{diameter}")


#sa_cylinder=2*3.14*radius*(radius+height)
c=-(csa/(2*3.14))
b=height
a=1
#discriminant
d=(b**2)-(4*a*c)
radius1=(-b+math.sqrt(d))/(2*a)
#print("radius1:",radius1)
diameter=2*radius1
print(f"diameter in case of surface area is:{diameter}")

