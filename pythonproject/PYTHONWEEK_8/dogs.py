class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age =age
        self.weight= weight
    def bark(self):
        return self.name
        print(f'{self.name}is barking')
    def run_speed(self,weight ,age):
        return weight/age*10
    def other_dog(self,fight):
            self.fight = fight
dog1 = Dog("charlie",3,10)
dog1.bark()
dog1.run_speed(20,2)
dog1.other_dog(1)