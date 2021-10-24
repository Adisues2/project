
from typing import List

class MenuManager:
    
    def __init__(self):
    
        self.dict = {}
    def add_item(self,name,price,spice,gluten):
        self.name= name
        self.price =price
        self.spice =spice
        self.gluten = gluten
        for item in self.dict:
            self.dict.append(item)
    def __str__(self):
        return {self.name}-{self.price}-{self.spice}-{self.gluten}
      
      
                                            
    def update_item(name,price,spice,gluten):
        for dish in dict():
        
            return dish.uppdate(dict)
        else:
            print(f"dish is not in the menu")
            
            
    def remove_items(self,name):
        for name in self.dict:
         dict.remove(name)
        else:
         print(self.dict)

menu = MenuManager()
menu.update_item("salad",20,False)
menu.add_item("Ham",15,"A",True)
print(menu.remove_items('soup'))



