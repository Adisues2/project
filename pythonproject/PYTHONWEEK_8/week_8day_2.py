
# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color1 = "blue"

# nc = NewCircle
# print(nc.color)


# class Door:
#     def __init__(self,is_open:bool):
#         self.is_open =is_open
#     def open_door(self):
#         print(f"is opening door")
#         self.is_open = True
#     def close_door(self):
#         print(f"is closing door")
#         self.is_open = False
        
# class BlockedDoor(Door):
#     def open_door(self):
#          raise Exception("cant oepn the door")
#     def close_door(self):    
#         raise Exception("cant oepn the door")
    
# door = Door(is_open=True)
# print(door.is_open)
# door.close_door()
# print(door.is_open)


# door.open_door()
# print(door.is_open)

# blocked_door = BlockedDoor(is_open=False)
# # blocked_door.open_door()
# blocked_door.close_door() 
# class A():
    
#     def dothis(self):
#         print("doing this in A")


# class B(A):
#     pass


# class C():
#     def dothis(self):
#         print("doing this in C")


# class D(C, B):
#     pass

# d_instance = D()
# d_instance.dothis() 

# week_8 excercises

# class Cat:
#     def __init__(self,name,age):
        
#         self.name =name
#         self.age = age
#         print(f"i am a cat of {self.name} and {self. age} years old")
      
#     def types_0f_cat(self):
#         print(f"i am a cat of {self.name} and {self.age} years old")
     
# cat1 = Cat("leo",4)
# cat1.types_0f_cat()
# cat2 = Cat("charlie",7)
# cat2.types_0f_cat()
# cat3 = Cat("bengalcat",5)
# cat3.types_0f_cat()

class Dog:
    def __init__(self,name,height):
        self.name =name
        self.height =height
    def bark(self,sound):
        self.sound =sound
        print(f"his name is {self.name} and  is love say {self.sound}")
        
    def jump(self , x = 2):
        print(f"{self.name} jumps  {self.height*2} cm high")
davids_dog = Dog("Rex",50,)
davids_dog.bark("woof")
davids_dog.jump()
sarahs_dog = Dog("Teacup",20)
sarahs_dog.bark("wowowu")
sarahs_dog.jump()
# if  (Dog  >=30):
#     print("{self.name} is bigger dog")
# else:
#     print("{self.name} is small dogs")
class Song:
    def __init__(self,lyrics):
        self.lyrics =lyrics
        self._index = -1
    def sing_me_a_song(self):
       self._index+=1
       if self._index>=len(self.lyrics):
           self._index =-1
           raise StopIteration
       else:
           return self.lyrics[self._index]
    def __reversed__(self):
        return self.lyrics[::-1]
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

for rev_lyrics in  reversed(stairway):
    print(rev_lyrics)
#     def __iter__(self):
#         return(_index for _index in self.lyrics)
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# for index in stairway:
#     print(index)

class Zoo:
    animals = []
    def __init__(self,zoo_name):
       
        self.zoo_name = zoo_name
        
    def add_animal(self,new_animal):
        self.new_animal = new_animal
        Zoo.animals.append(new_animal)
        print(f"animas in zoo {self.zoo_name} and {self.new_animal}")
       
        
    def get_animal(self):
        print(f"animals of zoo {self.zoo_name}")
    def sort_animal(self) ->list:
      
        return sorted(self.animals)
        # for i in animals:
        #     print(i)
    #   more questions left ....?
    
animal_num = Zoo("cat")
anima2_num = Zoo("Bear")
anima2_num.add_animal("cougar")
anima2_num.add_animal("Emu")
anima2_num.add_animal("bear")
anima2_num.get_animal()
anima2_num.sort_animal()
print(anima2_num.sort_animal())
print(animal_num.sort_animal())
class Circle:
    def __init__(self,radius :int= 1):
        self.radius = radius
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return self.radius**2*3.14
Circle1 =Circle(1)
print(Circle1.area())
print(Circle1.perimeter())




class Phone:
    def __init__(self,phone_number,message):
        self.phone_number = phone_number
        self.message = []
        self.call_history = []
    def call (self,other_phone):
        self.other_phone = other_phone
        print(f"who called who {self.other_phone}")     
    def show_call_history(self):
        return self.call_history
    def send_message(self):
         return self.message
    def  show_outgoing_messages(self):
          return self.call
phone1 =Phone("111","2345")
print()

# clas mydic :
#     def init()sekf,key,list.value:list)":
#     self.mydic = {}"
    
#     for i in range(len(mydci)):
    # self.mydic[keys[i]] =values[i]

#         temp = mydic{['key1','key']}
        
#         if(len(value) ==0):
#              for i in range(len(mydci)):
#                  self.mydic[keys[i]]=>None\
    # temp1 ={[key1,key2]]}