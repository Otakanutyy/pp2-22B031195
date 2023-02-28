import re
string=""
with open('C:\Users\Ислам\Documents\week1\pp2-22B031195\tsis5') as fo:
    for rec in fo:
        string=string+rec
        if rec==' ':
            #1task
            pattern = "ab*"
            if re.match(pattern, string):
                print("for first case:",string)
            string=""
    string=""
    for rec in fo:
        string=string+rec
        if rec==' ':
            #2 task
            pattern1 = "ab{2,3}"
            if re.match(pattern1, string):
                print("for second case:", string)
            string=""
string=""

with open('C:\Users\Ислам\Documents\week1\pp2-22B031195\tsis5') as fo:
    #3 task
            pattern2 = r"\b[a-z]+(_[a-z]+)*\b"
            matches = re.findall(pattern2, fo)
            if matches:
                print("for third case:")
                for match in matches:
                    print(match)


with open('C:\Users\Ислам\Documents\week1\pp2-22B031195\tsis5') as fo:
    pattern3 = r"[A-Z][a-z]+"
    matches1 = re.findall(pattern3, fo)
    if matches:
        print("for forth case:")
        for match in matches:
            print(match)

with open('C:\Users\Ислам\Documents\week1\pp2-22B031195\tsis5') as fo:
    for rec in fo:
        string=string+rec
        if rec==' ':
             pattern4 = r"a.*b$"
             match = re.search(pattern, string)
             if match:
                 print("for fifth case:", match.group())
            string=""

string=""


   


