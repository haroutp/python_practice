# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# HINT:
#  a. Think of what inputs will you need from the user
#  b. How will you determine what type the triangle is?

# Define the types of triangles for yourself and the user
str_equilateral_definition = "all angles are equal."
str_isosceles_definition = "two angles are equal."
str_scalene_definition = "no angles are equal."

# Make sure the user can only input integers and not strings
try:
    int_angle_01 = int(input("Tell me the 1st angle: "))
    print("This is a valid number! Angle 01 is...", int_angle_01)
    int_angle_02 = int(input("Tell me the 2st angle: "))
    print("This is a valid number! Angle 02 is...", int_angle_02)
    int_angle_03 = int(input("Tell me the 3st angle: "))
    print("This is a valid number! Angle 03 is...", int_angle_03)
except ValueError:
    print("This is not a valid number. It isn't a number at all! This is a string.. Try again!")

 # Run an if statement
if int_angle_01 == int_angle_02 == int_angle_03:
    print("You have an equilateral triangle! That means", str_equilateral_definition)
elif int_angle_01 == int_angle_02 != int_angle_03 or int_angle_03 == int_angle_02 != int_angle_01:
    print("You have an isosceles triangle! That means", str_isosceles_definition)
else:
    print("You have a scalene triangle! That means", str_scalene_definition)




