import math  
  
def CA (Radius):   
    area = Radius** 2 * math.pi  
    return area  
  
Radius = float (input ("Enter the radius of the circle: "))  
print (" The area of the circle is: ", CA (Radius))  