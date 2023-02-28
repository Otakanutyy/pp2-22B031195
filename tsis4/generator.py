#1
def square_generator(k):
    for i in range(1, k+1):
        yield i*i

k=int(input())
for square in square_generator(k):
    print(square)

#2
def even_generator(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n=int(input())
even_nums= even_generator(n)
print(*even_nums, sep=",")

#3
def divisible_numbers(b):
    for i in range(b+1):
        if i%3==0 and i%4==0:
            yield i

b=int(input())
divisble_nums=divisible_numbers(b)
print(*divisble_nums, sep=" ")


#4
def squares2(a, b):
    for i in range(a, b+1):
        yield i*i

a=int(input())
b=int(input())
for square2 in squares2(a,b):
    for l in range (a, b+1):
        if l*l==square2:
            print(square2)

    

#5
def decrementing(p):
    while p>=0:
        yield p
        p-=1

p=int(input())
for dec in decrementing(p):
    print(dec)