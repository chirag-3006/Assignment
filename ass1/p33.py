#33. A rectangular garden has dimensions of 30 m
#by 20 m and is divided in to 4 parts by two pathways
#  that run perpendicular from its sides. One pathway has a width of 3 m and
#  the other, 4 m. Calculate the total usable area of the garden.

#recatangular dimenstion
length=30
breadth=20
total_area_rect_garden=length*breadth
print(f"total dimesion:{total_area_rect_garden}")

#firstpathway
width=3
length=30
area_first_pathway=width*length

#secondpathway
width=4
length=20
area_Second_pathway=width*length

#ovelapping pathway
length=3
breadth=4
area_overlap_pathway=length*breadth

#total pathway
total_area_pathway=area_first_pathway+area_Second_pathway-area_overlap_pathway

#garden
garden_dimesion_withoutpathway=total_area_rect_garden-total_area_pathway
print(f"only garden dimeansion is:{garden_dimesion_withoutpathway}")

