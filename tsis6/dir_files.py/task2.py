import os
p=os.listdir(r"C:/Users/Ислам/Documents/week1/pp2-22B031195")

print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))