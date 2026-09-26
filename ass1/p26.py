
#How many bricks will be required to lay a path 120 m long and 2.4 m 
# breadth if a brick is 24 cm long and 15 cm wide?

#path
length=120*100
breadth=2.4*100
area_path=length*breadth

#brick
length2=24
breadth2=15
area_brick=length2*breadth2

no_of_bricks=int(area_path/area_brick)
print("no of bricks:",no_of_bricks)
