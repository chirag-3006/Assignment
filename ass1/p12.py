#12. Find the area of a right angled triangle whose hypotenuse is 13 cm 
# and one of its sides containing the right angle is 12 cm. 
# Find the length of the other side.

import math

hypotenous=13
perpendicular=12
base= (13*13)-(12*12)
base=int(math.sqrt(base))
print(f"base:{base}")
