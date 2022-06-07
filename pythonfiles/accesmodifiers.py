#https://www.youtube.com/watch?v=aeOu3RWOWAI

class Person:
    __name = None
    __age =  None 
    
    def __init(self, name, age):
        self.__name = name 
        self.__age = age 
    
    def __print_details(self):
        print ("Name =", self.__name)
        print ("Age = ", self.__age)
    

#Object of class Person

person_object = Person("Rashi", 25)

# print(person_object.name, person_object.age)
print(person_object.__print_details())


    


    

       


