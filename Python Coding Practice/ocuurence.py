list=[11,12,19,19,5,5,5,13]
count1=0
count2=0

for i in list:
  if i == 19:
    count1 = count1+1
  elif i == 5:
    count2=count2+1
if count1 == 2 and count2>=3 :
  print( "True")
else:
  print("False")