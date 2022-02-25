import trignometry as tri

tri_area, unit = tri.area_of_triangle(10,15)
print(f"Area of triangle  is {tri_area} {unit}")
if tri_area > 100:
    
    print("It is a big trianle")

else:

    print("It is a small triangle")

print(tri.check_right_triangle(10,12,15))