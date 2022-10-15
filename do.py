row = 4
col = 4
tot = row * col
list = []
num = 0
diff = num + 1
for i in range(row):
    ele = []
    for j in range(col):
        if  j == 0:
            num = i + diff
            ele.append(num)
        elif i+ 1 == row and j+ 1 == col:
            ele.append(tot)
        else:
            if diff < row:
                diff += 1
                num = num + diff + i
                ele.append(num)
            else:
                num = num + diff
                ele.append(num)
    diff = i
    diff += 1
    num += i
    list.append(ele)

for i in range(row):
    for j in range(col):
        print(list[i][j],end="\t")
    print()
