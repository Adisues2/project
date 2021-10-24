from typing import List
class Human:
    def __init__(self,name:str,age:int,living_place:None):
        self.name =name
        self.age = age
        self.living_place  = living_place
    def add_move(self,building):
        self.living_place = building
        building.inhabitants.append(self)
       
        
class Building:
    def __init__(self, address:str ,inhabitants: list = None):
        self.address = address
       
        if not inhabitants:
            inhabitants = []
        self.inhabitants = inhabitants
class City:
    def __init__(self,name:str ,buildings):
        self.name = name
        self.buildings = buildings
    def construct(self,address):
        # self.address = address
        
        new_building = Building(address)
        self.buildings.uppdate(new_building)
    def add_info(self,address):
        print(f"the number if buildings is {self.buildings}")
        total_age = 0
        total_citizens = 0
        for building in self.buildings:
            total_citizens+=  len(building.inhabitants)
            for human in building.inhabitnats:
                total_age += human.age
            print(f"the mean age is{total_age/total_citizens}")
         
         
         
# human = Human("teliviv",4 ,"holon")
# human.add_move("yield")
city = City("floor","allenby")
city.construct('teiviv')

         