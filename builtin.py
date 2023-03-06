import math
#1
list=list(input("Enter numbers separated by space ").split())
list = [int(i) for i in list]
print(math.prod(list))

#2
string1=input("Enter string: ")
lower=0
upper=0
for char in string1:
    if char.isupper():
        upper+=1
    else:
        lower+=1
print("upper: ",upper," ","lower: ",lower)

#3
s=input("Enter string to check: ")
s = s.lower().replace(" ", "")
if (s == "".join(reversed(s))):
    print("Yes")
else:
    print("No")

#4
import time
n=int(input())
time1=int(input())
time.sleep(time1/1000)
print(math.sqrt(n))

#5
t = tuple(input('Enter space-separated words: ').split())
print(all(t))