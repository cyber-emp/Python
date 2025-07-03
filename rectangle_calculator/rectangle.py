# create a basic operation. rectangle area and perimeter calculator
# must ask user length and width of rectangle

# need to use functions and modules and must be imported

import calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculator.area(length, width)
perimeter = calculator.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")
# This code imports the calculator module and uses its functions to calculate the area and perimeter of a rectangle based on user input.