a = [1,2,3]
b = [3,2,1]
 
c = [0]*2

for i in range(3):
    if a[i]>b[i]:
        c[0]=1
    elif a[i]==b[i]:
        continue;
    else:
        c[1]=1
print(c)
