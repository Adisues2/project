from typing import Dict


class Dog():
    number_of_dogs = 0
    dogs_king = "Bernie IV"
    def __init__(self, name_of_the_dog):
       
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1
        

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name
    def sortedDogs(self)->list:
        print(sorted(name))
    

my_dog = Dog("Rex")
my_dog2 = Dog("Bernie V")
my_dog1 =Dog("boby")

my_dog1.walk(5)
print("Curently, there are {} dogs".format(Dog.number_of_dogs))

class Circle:
    color = "red"

    def __init__(self, diameter):
        self.diameter = diameter
       
    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color)
print(Circle.color)
print(circle1.get_color())
circle1.grow(3)
print(circle1.diameter)
# @g
class MyClass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return self.first_name+self.last_name

    def email(self): 
        return "{}.{}@gmail.com".format(self.first_name,  self.last_name )

newClass = MyClass("John", "Doe")
print(newClass.email())
newClass.email = "smith"
print(newClass.email)
print(newClass.first_name)
print(newClass.last_name)
print(newClass.full_name())


def power(a, b):
    """Returns arg1 raised to power arg2."""
  
    return a**b
  
print(power.__doc__)
class MyClass(object):
    count = 5

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 5

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 5
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)
print(b.val)
print(c.val)
print(a.filterint(100))

# name = input("enter the a name:")
# age  = int(input("enter age:"))
# score = int(input("enter a score:"))
name, age, score = input("Enter student's name, age and score separated by space:").split()
print("Student Name:", name)
print("Student Age:", age)
print("Student Score:", score)

word = (name,age,score)
# print(sorted(word)
print(sorted(word))
word = map(lambda word : name,age,score,word)
print(word)