from pprint import pprint

lst = []
n = 5

for i in range(n):
    temp_lst = []
    for j in range(n):
        if i == j:
            temp_lst.append(1)
        else:
            temp_lst.append(0)

    lst.append(temp_lst)

for row in lst:
    #print(row)
    line = list(map(str, row))
    #print(line)
    line_str = ' '.join(line)
    print(line_str)


#print(lst)
