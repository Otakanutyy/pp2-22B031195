cake_list=['plum cake', 'Ferrero cake', "Big cake", "White cake"]
print(cake_list)
textfile=open('C:/Users/Ислам/Documents/week1/pp2-22B031195/tasks/listtext.txt', 'w')
content = '\n'.join(cake_list)
textfile.writelines(content)