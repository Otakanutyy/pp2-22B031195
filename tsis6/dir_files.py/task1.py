import os
p=os.listdir(r"C:/Users/Ислам/Documents/week1/pp2-22B031195")

for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)