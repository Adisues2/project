# key = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# for key in zip( key, values):
#     print(key)
# # person = int(input("theater charges different ticket"))
# for age in range(person):
#     if age <3:
#         print("ticket is free")
#     if age <13:
    
#         print("the ticket is $10")
#     if age > 12:
#         print("the ticket is $15")
#     family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#     print(family)
   



brand = {
        "name": "Zara ",
   " creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona ",
  "type_of_clothes": "men, women, children, home" ,
  "international_competitors":" Gap, H&M, Benetton", 
  " number_stores": 7000 ,
  "major_color": 
    "France" "blue",
    "Spain": "red" ,
     "US" :"pink" "green"
     } 
# print(brand["name"])  
# brand[" number_stores"] = 2
# print(brand[" number_stores"]) 
# print(brand)

# brand["country_creation"] = "span"
# print(brand)
# for international_competitors in brand:
#     brand[" number_stores"] = "Desigual"
#     print(brand)
del brand[" creation_date"]
print(brand)
print(brand["international_competitors"])
print(brand["major_color"])
for key  in brand:
    print(key)
    print(len(brand))

more_on_Zara = {
    "creation_date" : 1975,
    "number_stores":10000

}
print(more_on_Zara)
brand["more_on_Zara"] =  {
    "creation_date" : 1975,
    "number_stores":10000

}
print(brand)

# print(brand["number_stores"])
import datetime
# birthday = {
#     "john" : 12490,
#     "smith": 23698,
#     "jones" : 11278,
#     "alex" : 24670
# }
# birthday = input('Enter your birthday in dd/mm/yyyy format')
# user = str(birthday)
# print("You can look up the birthdays of the people in the list!")

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(items)
for key in items:
    print(key)

    l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
s = l2.count(4)
print(s)
d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
for key ,value in d.items():
 print(f"the key {key}   and the value {value}" )


 
 myList = [10, 25, 17, 9, 30, -5]
 myList2 =map(lambda n : n*2,myList)
 print(myList2)