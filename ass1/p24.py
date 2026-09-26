#24. How many bricks each 25 cm long, 10 cm wide and 7.5 cm thick will be 
# required for a wall 20 m long, 2 m high and 0.75 m thick? 
# If bricks sell at $900 per thousand what will it cost to build the wall?

length=25 
breadth=10
height=7.5
bricks_volume=length*breadth*height
print(f"volume of brick:{bricks_volume}cm^3")

#volume of wall
length=2000
breadth=200
height=75
walls_volume=length*breadth*height
print(f"volme of wall:{walls_volume}")

no_of_bricks=int(walls_volume/bricks_volume)
print(f"no of bricks:{no_of_bricks} bricks")

cost_wall=int((no_of_bricks*900)/1000)
print("cost of making wall:",cost_wall)