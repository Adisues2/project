
import json
class MenuManager:
    def __init__(self,menu):
        self.menu =menu
        menu =  open("restuarant_menu.txt","r")
        return  menu.read()
    def add_items(self,name,price):
        menu = []
        for i in range(list(name)):
            menu.append(name[i],price[i])
            return  menu
    def remove_items(self,name):
        if name in range( list(menu)):
            menu.remove(name)
            return  True
        else:
            return False

    def save_file(self):
         return  menu


data  = MenuManager("stiff")
data.add_items("stif",45)

