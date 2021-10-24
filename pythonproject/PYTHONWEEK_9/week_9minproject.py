class Character:
    def __init__(self,name,attack:int =10,life:int =20):
        self.name = name
        self.attack = attack
        self.life =life
        print(f"creating the chatacter:{name} and life{life} and the attack by{attack}")
    def basic_attack(self,other_char):
        other_char.life -=self.attack

     
class Druid(Character):
    
    def mediate(self ,life : int = 10, attack: int= 2):
       
           self.life +=10
           self.atack -= 2
        
    def animal_help(self):
            self.attack +=5
      
    def fight(self,other_char):
     
        other_char.life = (0.75*self.life+0.75*self.attack)
class Warrior(Character):
    
    def brawl(self,other_char):
        other_char = (2 * self.attack )
        life        = ( 0.5 *self.attck)
    def train(self):
        self.attack  +=2
        self.life  +=2
    def roar(self,other_char):
        other_char -=3
class Mage(Character):
    def curse(self,other_char):
        other_char.attack -= 2
    def summon(self):
        self.attack +=3
    def cast_spell(self,other_char):
        self.other_char.life -= self.attack/self.life
character_game1 = Mage("hyena", attack = 80, life = 50 , )   
character_game2 =Warrior("jack",attack = 70, life = 50)

character_game3 =Druid("nam",attack = 60, life = 55)
print(character_game1.attack)

character_game1.curse(character_game2)
print(character_game2.attack)
character_game3.fight(character_game1)
print(character_game1.life)

# def add_to_dict(my_dict):
#     my_dict['key1'] = 'val1'
# d = {}
# print(d)
# add_to_dict(d)
# print(d)

