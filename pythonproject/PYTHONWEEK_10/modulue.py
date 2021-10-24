import json


class MenuManager():

    def __init__(self):

        menu = "week_10day4/retuarant_menu.json"
        json_file = json.dumps(menu)

    def add_items(name, price):
        menu = name, price
        return menu.append("add_items")

    def remove_items(name):

        if name in menu:
            del name
        else:
            return False


manager = MenuManager()
MenuManager.add_items('vegetable soup', 30)



