a = [[4, 6, 7],
     [2, 3, 4],
     [1, 2, 2]]

b = [[9, 8, 9],
     [2, 3, 4],
     [1, 2, 2]]


listprod = []
for i in range(len(a)):
    for j in range(len(b)):
        listprod.append(a[i][j] * b[i][j])


print(listprod)

