file1=open("C:/Users/Ислам/Documents/week1/pp2-22B031195/python_test/copyfrom.txt")
file2=open("C:/Users/Ислам/Documents/week1/pp2-22B031195/python_test/copyto.txt")
file=open(file1,"r")
data=file.read()
file.clos()

with open(file2, "a") as file:
    file.write(data)

 