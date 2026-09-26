#43. Find the cost of polishing the base of a cone
#  whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm
import math
height=4
slant_height=5
radius=math.sqrt((slant_height**2)-(height**2))
print("radius",radius)
area_of_circle=3.14*(radius**2)
cost_of_polishing_base=10*area_of_circle
print(f"cost of polishing:{cost_of_polishing_base}")