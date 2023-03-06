import re
#1
pattern1= re.compile(r'a+b*')
print(pattern1.match(input()))

#2
pattern2 = re.compile(r'a{1}b{2,3}')
print(pattern2.match(input()))

#3
pattern3 = re.compile(r'[a-z]+_[a-z]+')
print(pattern3.match(input()))

#4
pattern4 = re.compile(r'[A-Z]{1}[a-z]+')
result = pattern4.findall(input())
print(result)

#5
pattern5 = re.compile(r'a.+b\Z')
result = pattern5.search(input())
print("correct") if result != None else print("not correct")

#6
pattern6 = re.compile(r'[ .,]')
result = pattern6.sub(":", input())
print(result)

#7
text7 =input()
def snake_to_camel(text):
    snake=re.findall('[a-z]+',text)
    camel=""
    for i in snake:
        camel+=i[0].upper()+i[1:len(i)]
    return camel

print(snake_to_camel(text7))

#8
pattern8 = re.compile(r'[A-Z]')
n = input()
print(pattern8.split(n))

#9
text9 = input()
print(re.sub(r"(\w)([A-Z])", r'\1 \2', text9))

#10
text10 = input()
step1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text10)
step2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', step1).lower()
print(step2)