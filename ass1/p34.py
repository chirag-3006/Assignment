#34. A wooded area is in the shape of a a trapezoid whose
#  bases measure 128 m and 92 m and its height is 40 m. 
# A 4 m wide walkway is constructed which runs perpendicular to the two bases. 
# Calculate the area of the wooded area after the addition of the walkway.

#trapezoid_before
base1=128
base2=92
h=40
area_of_trapezoid=((base1+base2)*40)/2

#constructed_walkway
area_walkway=4*40

#wooden_trapezoid_after
wooden_area=area_of_trapezoid+area_walkway
print(f"wooded area is:{wooden_area}")


