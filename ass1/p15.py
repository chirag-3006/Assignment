
'''15. Shelly has a rectangular garden of length 22 m
and breath 15 m. Her friend Rachel has a square garden of side 21 m.
Whose garden is bigger and by how much?'''
length=22
breadth=15

shelly_garden_area=length*breadth
print(shelly_garden_area)
side=21
rahel_garden=side*side
print(rahel_garden)
if(shelly_garden_area>rahel_garden):
    print(f"shelly garden is greater:")
else:
    print(f"rahel garden is greater")