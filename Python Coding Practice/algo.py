# FIBONACCI SERIES
from array import ArrayType, array


print("Fibonacci Numbers ahead, beware!!")
print("\n")

f = [0, 1]

for x in range(2, 10):
    f.append(f[x-1] + f[x-2])
    print(f)

print("\n")
# FACTORIAL OF A NUMBER
print("------------------------")
print("Factorial code ahead, beware!!")
print("\n")


def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * fact(n - 1)


num = 5
print("Factorial of", num, "is", fact(num))

print("\n")
# FACTORS OF A NUMBER
print("------------------------")
print("Factorization code ahead, beware!!")
print("\n")


fac = 330
a = [1]
for i in range(1, fac+1):
    if fac % i == 0:
        a.append(i)

print(a)

print("\n")
# PRIME NUMBERS
print("------------------------")
print("Prime numbers code ahead, beware!!")
print("\n")

num = 21
temp = 1
if num == 0 or num == 1:
    print('neither prime nor composite')
else:
    for i in range(2, num-1):
        if num % i == 0:
            temp = 2
            break

if temp == 2:
    print(num, 'is not prime')
else:
    print(num, 'is prime')


print("\n")
# SELECTION SORT
print("------------------------")
print("Selection sorting ahead, beware!!")
print("\n")

A = [243, 89, 293, 93, 123]

for i in range(len(A)):
    min = i
    for j in range(i+1, len(A)):
        if A[min] > A[j]:
            temp = A[min]
            A[min] = A[j]
            A[j] = temp

print(A)


print("\n")
# BUBBLE SORT
print("------------------------")
print("Bubble sorting ahead, beware!!")
print("\n")


def swap(a, b):
    a, b = b, a
    # temp=a
    # a=b
    # b=temp
    # return a,b;


for i in range(0, len(A)):
    for j in range(0, len(A)):
        if (A[j] > A[j+1]):
            # A[j], A[j+1] = A[j+1], A[j]
            swap(A[j], A[j+1])
        else:
            break
print(A)


print("\n")
# LINEAR SEARCH
print("------------------------")
print("Linear Search ahead, beware!!")
print("\n")
# copied


def search(arr, n, x):

    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 40
n = len(arr)

# Function call
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result+1)


print("\n")
# BINARY SEARCH
print("------------------------")
print("Binary Search ahead, beware!!")
print("\n")


def binSearch(l, h, x):
    if h >= l:
        m = l+(h-l) // 2

        if x == AR[m]:
            return m
        elif x < AR[m]:
            return binSearch(l, m-1, x)
        elif x > AR[m]:
            return binSearch(m+1, h, x)

    else:
        return -1


AR = [90, 100, 104, 1000, 9090]
low = 0
high = len(AR)
x = 1000

res = binSearch(low, high, x)
print("result =", res)


print("\n")
# MEDIAN OF TWO UNEQUAL SORTED ARRAYS
print("------------------------")
print("Median code ahead, beware!!")
print("\n")


arr1 = [10, 22, 39, 89, 90, 103, 400]
arr2 = [23, 40, 50, 68, 100]

sum_of_lengths = len(arr1)+len(arr2)

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0
k = 0


def new_func(n1, n2):
    arr3 = [None] * (n1 + n2)
    return arr3


def mergedarr(arr1, arr2, n1, n2):
    arr3 = new_func(n1, n2)
    i = 0
    j = 0
    k = 0
   # Traverse both array
    while i < n1 and j < n2:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i]
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j]
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end=",")
    return arr3


merged = (mergedarr(arr1, arr2, n1, n2))


if (sum_of_lengths) % 2 == 0:
    median = int((sum_of_lengths/2)-1)
    print('median = ', (merged[median]+merged[median+1])/2)
else:
    median = int(sum_of_lengths/2)
    print('median = ', merged[median])


print("\n")
# Stack implementation
print("------------------------")
print("Stack implementation ahead, beware!!")
print("\n")
# copied

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)


print("\n")
# String Manipulation functions
print("------------------------")
print("String Manipulation functions ahead, beware!!")
print("\n")


string = 'my nAme is rashi'

st = string.replace('rashi', 'toshi', 1)
print(st)

print(string.capitalize())
print(string.casefold())
print(string.center(33, '$'))
print(string.title())
print(string.encode)


print("\n")
# interpret function
print("------------------------")
print("Interpret Function ahead, beware!!")
print("\n")


def interpret(s):

    mydict = {"G": "G", "()": "o", "(al)": "al"}
    res = ""
    temp = ""
    for i in range(len(s)):
        temp += s[i]
        if temp in mydict:
            res += mydict[temp]
            temp = ""

    return res


s = "G()(al)G()(al)"
print(interpret(s))


print("\n")
# Iterative Binary Search function
print("------------------------")
print("Iterative Binary Search Function ahead, beware!!")
print("\n")


def search(nums, target) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        pivot = left + (right-left) // 2

        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot-1
        else:
            left = pivot + 1
    return -1


output = search([-1, 0, 3, 5, 9, 12], 9)
print(output)


# Max Palindrome possible Count of chars:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()

        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)

        return pairs * 2 + 1 if unpaired_chars else pairs * 2
