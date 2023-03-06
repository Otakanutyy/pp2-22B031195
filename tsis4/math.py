import math
#1
deg=int(input())
print(math.radians(deg))

#2
print("Enter height:")
h=int(input())
print("Enter base1:")
b1=int(input())
print("Enter base2:")
b2=int(input())
print((b1+b2)/2*h)

#3
print("Enter num of sides:")
num=int(input())
print("Enter len of sides:")
l=int(input())
area=(num*l*l)/(4*math.tan(math.pi/num))
print(area)

#4
b3=float(input("Enter base:"))
h2=float(input("Enter height"))
area2=b3*h2
print(area2)