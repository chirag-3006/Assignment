#29. How many square tiles of side 10 cm will be required 
# to tile a floor measuring 800 cm by 900 cm?

square_side=10
area_square=square_side*square_side

floor_length=800
floor_breadth=900
area_floor=floor_length*floor_breadth

no_of_square_tiles=int(area_floor/area_square)
print(f"no_of_square_tiles:{no_of_square_tiles}")