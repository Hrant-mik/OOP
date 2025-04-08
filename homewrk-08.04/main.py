# --------------------------------------------- Employee Inheritance  ---------------------------------------------
"""Create an Employee class with name and salary. Create a Manager subclass that adds a team_size attribute."""
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def __str__(self):
#         return f"Name : {self.name}, salary : {self.salary}"
    
# class Maneger(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size
        
#     def __str__(self):
#         return f"Name : {self.name}, salary : {self.salary}, team size : {self.team_size}"
        
# maneger = Maneger("Hrant", 500000, 9)
# print(maneger)




"""-------------------------------------------- Person and Student ------------------------------"""
"""Create a Person class with name and age. Create a Student subclass that adds grade."""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"Name : {self.name}, Age : {self.age}"
    
# class Student(Person):
#     def __init__(self, name, age, greade):
#         super().__init__(name, age)
#         self.greade = greade
        
#     def __str__(self):
#         return f"Name : {self.name}, Age : {self.age}, Greade : {self.greade}"
    
# student = Student("Hrant", 21, 9)
# print(student)



"""Create an Appliance class with power_on() and power_off(). Create a TV subclass that overrides power_on()."""

# class Appliance:
#     def power_on(self):
#         print("The appliance is ON.")

#     def power_off(self):
#         print("The appliance is OFF.")


# class Tv(Appliance):
#     def power_on(self):
#         print("The TV is ON.")
        
        
# tv = Tv()
# tv.power_on()



"""Create a BankAccount class with balance. Create SavingsAccount and CheckingAccount subclasses with different withdraw() rules."""

class Bankaccount:
    pass




"""Create a Player class with name and sport. Create Footballer and Basketballer subclasses with different play() methods."""

# class Player:
#     def __init__(self, name, sport):
#         self.name = name
#         self.sport = sport
        
# class Footballer(Player):
#     def __init__(self, name, sport):
#         super().__init__(name, sport)
    
#     def play(self):
#         return f"{self.name} has great ball skills:"
        
# class Basketballer(Player):
#     def __init__(self, name, sport):
#         super().__init__(name, sport)
        
#     def play(self):
#         return f"{self.name} is excellent at throwing the ball into the net."
    
# footballer = Footballer("Messi", "footballer")
# print(footballer.play())
# basketballer = Basketballer("Jordan", "basketballer")
# print(basketballer.play())


"""Create a Book class with title and author. Create an EBook subclass that adds file_size."""

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}"

# class Ebook(Book):
#     def __init__(self, title, author, file_size):
#         super().__init__(title, author)
#         self.file_size = file_size
    
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, File size: {self.file_size}"

# ebook = Ebook("Shun u katu", "Tumanyan", 60)
# print(ebook)


"""Create a Pet class with a sleep() method. Create Dog and Cat subclasses that override sleep() to specify different sleeping styles."""

# from abc import ABC, abstractmethod

# class Pet:
#     @abstractmethod
#     def sleep(self):
#         pass

# class Dog(Pet):
#     def sleep(self):
#         print("Dog sleep - zzzzzzzzzzzzzzzzzzzzzz!!!!!!!!!!!")
        
# class Cat(Pet):
#     def sleep(self):
#         print("Cat sleep - dz-------dzzzzzzzzd--zdzdzdzdz!!!!!!")

# dog = Dog()
# dog.sleep()

# cat = Cat()
# cat.sleep()


"""Create a Parent class with a message() method. Create a Child subclass that overrides message()."""

# class Parent:
#     def message(self):
#         print("This is a Parent class")
        
# class Child(Parent):
#     def message(self):
#         print("This is a child class")
    
# child = Child()
# child.message()



"""Create a BankAccount class with a get_fees() method. Create a PremiumAccount subclass that overrides get_fees() to return lower fees."""

# class Bankacaunt:
#     def __init__(self, many):
#         self.many = many
        
#     def get_fees(self):
#         return "Your fiss: 0.1%"
    
# class Premiumaccount(Bankacaunt):
#     def __init__(self, many):
#         super().__init__(many)
#     def get_fees(self):
#         return "Your fiss: 0.5%"
    
# premium = Premiumaccount(25000)
# print(premium.get_fees())


"""Create a TrafficLight class with get_color() that returns "Red". Create a PedestrianLight subclass that overrides get_color() to return "Green"."""


# class Trafficligh:
#     def get_color(self):
#         return "Red"

# class PedestrianLight(Trafficligh):
#     def get_color(self):
#         return "Green"
    
# pedestrianLight = PedestrianLight()
# print(pedestrianLight.get_color())



"""Create an Employee class with get_bonus(). Create Manager and Intern subclasses that override get_bonus() with different values."""


class Emoloyee:
    def get_bonus(self):
        return "Your bonus is 15"
    
class Manager(Emoloyee):
     def get_bonus(self):
        return "Your bonus is 45"

class Intern(Emoloyee):
     def get_bonus(self):
        return "Your bonus is 86"