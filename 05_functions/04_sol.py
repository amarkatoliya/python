# create fun that return area and circumference
import math
radius = int(input("Enter Radius: "))

def cal_area_and_cir(radius):
    area = ((radius)**2)*math.pi
    cir = 2 * math.pi * radius
    return area, cir
    
a,c =cal_area_and_cir(radius)   
 
# math.round(a)

print("Area: ",round(a,3) ,"cir: ", round(c,3))    
    