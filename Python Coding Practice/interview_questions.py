# Question 1. Create a solution to obtain the top user of the RestAPI service of your domain.

listed = [['a', 123, 'customer2', 'abc'],
          ['b', 123, 'customer1', 'abc'],
          ['c', 123, 'customer2', 'abc'],
          ['d', 123, 'customer2', 'abc'],
          ['e', 123, 'customer2', 'abc'],
          ['f', 123, 'customer1', 'abc'],
          ['g', 123, 'customer2', 'abc'],
          ['g', 123, 'customer2', 'abc'],
          ['g', 123, 'customer3', 'abc']]
j = 0
list_of_customers = []
for i in listed:
    #print (i[0])
    list_of_customers.insert(j, i[2])
    j += 1

count = 0
i = 1
arr = []
max = list_of_customers.count(list_of_customers[0])

for i in range(len(list_of_customers)):
    if max <= list_of_customers.count(list_of_customers[i]):
        max = list_of_customers.count(list_of_customers[i])
        name = list_of_customers[i]
print(name, max)

#print(list_of_customers[i],list_of_customers[j], count+1)


# Question 2. Given a list of lists of Students and their marks obtined, find out the max average of the scores and print it as output.
# Question 3. Given a list of objects find the non repeated characrter from each word.
