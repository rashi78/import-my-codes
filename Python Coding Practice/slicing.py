li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

#cloning
list_copy = li[:]
print("After cloning: ",list_copy)