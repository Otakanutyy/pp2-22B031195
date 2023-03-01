import re
import os
string=""
with os.open('C:/Users/Ислам/Documents/week1/pp2-22B031195/tsis5/row.txt') as fo:
    for rec in fo:
        string=string+rec
        if rec==' ':
            #1task
            pattern = "ab*"
            if re.match(pattern, string):
                print("for first case:",string)

# with open('C:/Users/Ислам/Documents/week1/pp2-22B031195/tsis5/row.txt') as fo:
#         pattern2 = r"\b[a-z]+(_[a-z]+)*\b"
#         matches = re.findall(pattern2, fo)
#         if matches:
#             print("for third case:")
#             for match in matches:
#                 print(match)


# with open('C:/Users/Ислам/Documents/week1/pp2-22B031195/tsis5') as fo:
#     pattern3 = r"[A-Z][a-z]+"
#     matches1 = re.findall(pattern3, fo)
#     if matches:
#         print("for forth case:")
#         for match in matches:
#             print(match)

# with open('C:/Users/Ислам/Documents/week1/pp2-22B031195/tsis5') as fo:
#     for rec in fo:
#         string=string+rec
#         if rec==' ':
#              pattern4 = r"a.*b$"
#              match = re.search(pattern, string)
#              if match:
#                  print("for fifth case:", match.group())



   


