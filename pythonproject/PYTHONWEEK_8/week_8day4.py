class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Persian(Cat):
    def walk(self):
        return super().walk()
    
my_cats = Cat("persians",4)  
print(my_cats.walk())
my_cats1 = Bengal("meowuwu",3)
print(my_cats1.sing("meewowu"))
my_cats2 = Chartreux("meeey",9)
print(my_cats2.sing("meey"))
    

class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age =age
        self.weight= weight
    def bark(self):
        
        print(f'{self.name} is barking')
    def run_speed(self,weight ,age):
        return weight/age*10
    def other_dog(self,fight):
            self.fight = fight
            return fight
dog1 = Dog("charlie",3,10)
dog1.bark()
print(dog1.age)
print(dog1.name)
print(dog1.weight)
print(dog1.run_speed(2,3))
print(dog1.other_dog("wowowu"))

import dogs
class PetDog:
    def __init__(self,trained:bool =False):
        trained 
        
    def bark(self):
        return True
    print("train")
dog1 = PetDog("boby")
dog1.bark()
