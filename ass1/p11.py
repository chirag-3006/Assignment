#The base and height of a triangle are in the ratio 8 : 5 and its area is 320 m². Find the height and base of the triangle.

area = 320
ratio_base = 8
ratio_height = 5

# Area = 1/2 × base × height
x = (2 * area / (ratio_base * ratio_height)) ** 0.5

base = ratio_base * x
height = ratio_height * x

print("Base =", base, "m")
print("Height =", height, "m")