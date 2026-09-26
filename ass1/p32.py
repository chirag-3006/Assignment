#32. A square garden with a side length of 150 m has 
# a square swimming pool in the very centre with a side 
# length of 25 m . Calculate the area of the garden.

#square_garden
side=150
whole_area_of_square_garden=side*side

#square_pool
side=25
area_of_pool=side*side

#areaofgarden
only_garden_area=int(whole_area_of_square_garden-area_of_pool)
print(f"area of garden:{only_garden_area}")

