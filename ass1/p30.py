#30. How many tiles of length 5 cm and breadth 8 cm are
#  needed to tile the floor of a bed room 200 cm long and 400 cm wide?

#tiles
length=5
breadth=8
area_tiles=length*breadth

#bedroomfloor
floor_length=200
floor_breadth=400
area_bedroom_floor=floor_length*floor_breadth

no_of_square_tiles=int(area_bedroom_floor/area_tiles)
print(f"no_of_square_tiles:{no_of_square_tiles}")