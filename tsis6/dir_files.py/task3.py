import os
p=(r"C:/Users/Ислам/Documents/week1/pp2-22B031195")

if os.path.exists(p):
    print("file and dir portions of the path")
    print(os.path.basename(p))
    print(os.path.dirname(p))
else:
    print("pass doesnt exist!")