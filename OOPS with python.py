     #whenever we declare insidena class it is called method

# class Student: #first character of classname must be capital
#     roll_number=101
#     num1 =50
#     num2 =100

#     def add(self):
#         print(self.num1+self.num2)
#         self.name=input("Enter name:") #name is your new type of variable
#         print(self.name)
# obj=student() #creating  a object of class and we always create a obj
# obj.add() #calling function
# print(obj.roll_number) #Accessing the data member of class by using obj

    #in class level or in function first argument must be self
    #By using construction we intialize the object
    #Assigning the memory address to object
    #constructer call automatically whenvever we create object
    #Here in python the name of constructor _int_(self)
    #for one object constructor will call one time

# class NewClass:
#     def __int__(self): #constructor  declaration (called Automatically)
#         print("constructor always execute first")
#     def show(self): #number function inside of class(It is a use define function)
#         print('Welcome to class level programming ')

# obj=NewClass() #creating a object
# #print(obj)
# obj.show()
# obj1=NewClass()

    #default construct
# class Hod:
#     def __init__(self):
#         self.name='prashant jha'
#         self.age=53
#         self.empid=1001

#     def info(self):
#         print("My name is :",self.name)
#         print("My Age is:",self.age)
#         print("My emp id:",self.empid)

# obj=Hod()
# obj.info()

    #parameter constructor
# class Hod:
#     def __init__(self,name,age,rollno):
#         self.age=age
#         self.rollno=rollno
#         self.name=name

#     def show(self):
#         print("My name is :",self.name)
#         print("My Age is:",self.age)
#         print("My rollno:",self.rollno)

# obj=Hod('Arjun',45,101)
# obj.show()

    #types os Variable 1.Instance Variable,2.static variable

# class New:
#     def __init__(self):
#         self.a=10

# Obj1 =New()
# Obj2= New()
# Obj3 =New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# Obj1.a=20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

       #Static variable is exactly opposite of instance variable
       #1 static variable = 1 memory 
       #How to access static variable? ->There are two ways to  access static variable the first one is by class name or second way 
       # by object but programmer recommended to access by class name.

# class New:
#     a=10

#     def __init__(self):
#         self.name="parshant"

# Obj1 =New()
# Obj2= New()
# Obj3 =New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)
# Obj1.a=50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

 #types of methodsin class are  1.class method,2.static method,instance method
 #Instance method:-If any instance variable we are implementing inside of any method then that method will be called as instance method

# class Student:
#     def __init__(self,name,mob,rollno):
#         self.mob=mob
#         self.rollno=rollno
#         self.name=name

#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob)

# stud=Student("Prashant",1001,6464646464)
# stud.display()

   #We can use static method when the code that belongs to class it do not use the object. 

class Student:  
    # by using class name we can access static method  
    @staticmethod # decorator  
    def get_personal_detail(firstname,lastname):  
        print("your personal detail=",firstname,lastname)  
  
    @staticmethod  
    def contact_detail(mobil_no, rollno):  
        print("your contact detail=", mobil_no,rollno)  
  
Student.get_personal_detail("prashant", "jha")  
Student.contact_detail(5456454646, 1001)