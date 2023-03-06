import os
p=(r"C:/Users/Ислам/Documents/week1/pp2-22B031195/tasks/probnik.py")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist!!!")