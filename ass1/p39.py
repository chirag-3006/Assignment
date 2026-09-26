#39. Find the surface of the cylinder if its diameter
#  is 12 centimeters and its height is 9 centimeters.

diameter=12
radius=diameter/2
height=9

sa_cylinder=2*3.14*radius*(radius+height)
print(f"surface of cylinder:{float(sa_cylinder)}")

csa=2*3.14*radius*height
print(f"csa:{float(csa)}")
