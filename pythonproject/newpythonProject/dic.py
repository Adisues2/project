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