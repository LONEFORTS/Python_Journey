#follwing program is to calculate surface volume and area of cylinder 

radius = int(input("Enter the Radius of the cylinder: "))  
height = int(input("Enter the Height of the cylinder: "))     

# Calculation formulas for the total surface area and volume of the cylinder                                              
 PI = 3.14

# The logic: Area of the outside shell + the two circles on top/bottom
total_surface_area = 2 * PI * radius * (radius + height)

# The logic: Base area (PI*r^2) multiplied by height
volume_of_cylinder = PI * (radius**2) * height

print(f"The Total surface area of the cylinder is: {total_surface_area}") 
print(f"The Volume of cylinder is : {volume_of_cylinder}")