#1
import math
degrees= float(input())
radians=math.radians(degrees)
print(radians)

#2
height=float(input("Enter height:"))
Base1=float(input("Enter base1:"))
Base2=float(input("Enter base2:"))
area=0.5*(Base1+Base2)*height
print(area)

#3
n= int(input("number of sides:"))
s=float(input("length of each side:"))
area2=(n*s**2)/(4*math.tan(math.pi/n))
print(area2)

#4
base=float(input("Enter base:"))
height2=float(input("Enter height"))
area3=base*height2
print(area3)