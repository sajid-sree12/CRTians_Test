import math
def calculate_area(name):
  name = name.lower()
  if name == "rectangle":
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))
    rect_area = l * b
    rect_perimeter=2*(l+b)
    print(f"The area of rectangle is{rect_area}.")
    print(f"The perimeter of rectangle is{rect_area}.")
  elif name == "square":
    s = int(input("Enter square's side length: "))   
    sqt_area = s * s
    sqt_perimeter=4*s
    print("The area of square is {sqt_area}.")
    print("The perimeter of square is {sqt_area}.")
  elif name == "cone":
    h = float(input("Enter cone height length: "))
    r = float(input("Enter cone radius length: "))
    con_area = 3.14*r*(r+math.sqrt(h*h+r*r))
    con_Volume = (1.0/3) * math.pi * r * r * h
    print(" The  Area of a Cone = %.2f " %con_area)
    print(" The Volume of a Cone = %.2f" %con_Volume)
  elif name == "circle":
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    circ_area = pi * r * r
    circ_perimeter = 2*pi*r
    circ_diameter = 2 * r
    circ_circumference = 2 * pi * r
    print("The area of circle is",circ_area)
    print("The perimeter of circle is", circ_perimeter)
    print(" Diameter Of a Circle = %.2f" %circ_diameter)
    print(" Circumference Of a Circle = %.2f" %circ_circumference)
  elif name == 'cylinder':
    r = float(input("Enter cylinder radius length: "))
    h = float(input("Enter cylinder height length: "))
    d = float(input("Enter cylinder diameter length: "))
    cyn_area = 2*math.pi*pow(r,2)*h
    cyn_perimeter = 2 * ( d + h ) 
    print("the area of a cylinder is %.2f" %cyn_area)
    print("the perimeter of a cylinder is %.2f" %cyn_perimeter)
  elif name == 'sphere':
    pi=3.14
    radian = float(input('Radius of sphere: '))
    sur_area = 4 * pi * radian **2
    volume = (4/3) * (pi * radian ** 3)
    diameter = 2* radian
    print("Surface Area is: ", sur_area)
    print("Volume is: ", volume)
    print("diameter is:",diameter)
  else:
    print("Sorry! This shape is not available")
if __name__ == "__main__" :
    print("Calculate Shape Area")
    shape_name = input("Enter the name of shape whose area you want to find: ")
calculate_area(shape_name)
