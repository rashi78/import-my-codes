arr1 = [10, 22, 39, 89, 90]
arr2 = [23, 40, 50, 110]

sum_of_lengths = len(arr1)+len(arr2)

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0
k = 0

mergedarr = [None] * (sum_of_lengths)
while (i < len(arr1)) and (j < len(arr2)):
    if (arr1[i] < arr2[j]):
        mergedarr[k] = arr1[i]
        k = k+1
        i = i+1

    else:
        mergedarr[k] = arr2[j]
        j = j+1
        k = k+1

while i < len(arr1):
    mergedarr[k] = arr1[i]
    i = i+1
    k = k+1

while j < len(arr2):
    mergedarr[k] = arr2[j]
    j = j+1
    k = k+1

for i in range(sum_of_lengths):
    print(str(mergedarr[i]), end=' ')
