#38. The cylinder has a volume of 1287. 
# The base has a radius 10. What is the area of the surface of the cylinder?

volume=1287
radius=10
height=volume/(3.14*(radius**2))
print("height:",height)

sa_cylinder=2*3.14*radius*(radius+height)
print(f"surface of cylinder:{float(sa_cylinder)}")

csa=2*3.14*radius*height
print(f"csa:{float(csa)}")