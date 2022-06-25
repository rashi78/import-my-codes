print ("\nHi, today we are going to learn about tuples and dictionaries in Python")

# A tuple is a set of elements which are ordered and immutable in nature. They allow duplicates. 
# Dictionary is a group of key-value pairs which is mutable in nature. It is unordered and they do not allow duplicates. 

tuple1 = (1,2,3,4,5)
print ("\n")
#dict1 = {tuple1[0]:"Shirin",tuple1[1]:"Rashi", tuple1[2]:"Toshi", 4:"Motuu", 5:"Prachi", 6:"Tanya" }
dict1 = {1:"Shirin", 2:"Rashi", 3:"Toshi", 4:"Motuu", 5:"Prachi", 6:"Tanya" }

#fromkeys is used to take the keys from an existing dict and create a new dict with same value assigned to each key

print(dict1.keys())
dict2= dict1.fromkeys(dict1.keys(), "new_value")
print ("\n")
print("New Dictionary: ", dict2)
print ("\n")
print(dict1.items())
print ("\n")



#As of Python version 3.7, dictionaries are ordered.
#In Python 3.6 and earlier, dictionaries are unordered.
##########################
#Type Definitions 

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



