a = [12,1,2,19,5,5,5,2,19]
#a = input()

print(a)
print(len(a))

def find_occurence(a):
  count_1=0
  count_2=0
  while (len(a)):
    for i in a:
      if a[i]==19:
        count_1 = count_1+1
        print(count_1)
      elif a[i]==5:
        count_2 = count_2+1
        print(count_2)
      else:
        i=i+1
  if count_1 == 2 and count_2 >=3:
    print ('true')
  else :
    print ('false')
