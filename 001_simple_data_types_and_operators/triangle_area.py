side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

half_perimeter = (side_a + side_b + side_c) / 2

triangle_area = (half_perimeter * (half_perimeter - side_a) *
                (half_perimeter - side_b) *
                (half_perimeter - side_c)) ** 0.5

print("Side A = " + str(side_a))
print("Side B = " + str(side_b))
print("Side C = " + str(side_c))
print("Area of triangle is " + str(triangle_area))
