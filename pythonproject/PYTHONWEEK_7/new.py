
# numbers =[11,23,14,14]
# for number in numbers:
#      if number == 14:
#        numbers[numbers.index(14)] = 0
# print(numbers)
# for i in range(0, len(numbers)):
#      if numbers[i] == 14:
#         numbers[i] = 0
# print(numbers)
# num = int(input("enter the number"))
# print("multiplications table of " ,sum)
# for i in range (num):
#     print(num,"x",i,"=" ,num*i)
# num = int(input("enter the number"))
# for i in range(num):
#      print(num*i)
# number_1 = 1
# while number_1<= 10:
#     print(number_1)
#     number_1+= 1
#     print("checked")
# daily challenge

# words= (input("enter string character")

# str_s = input("enter the string")
# if len(str_s) < 10:
#     print("string noit long enough")
# elif len(str_s)>10:
#     print("not enough")
#
# str_s = input("enter the string")
# length = len(str_s)
# for i in range(length):
#     print(str_s[:i + 1])


# import random
# str = input("")
# random.shuffle(str)
# favorite numbers
# my_fav_numbers = ["2","4","6","8","12","14","16"]
# my_fav_numbers.append("20", )
# print(my_fav_numbers)
# my_fav_numbers.remove("20")
# print(my_fav_numbers)
# friend_fav_numbers = ["3", "5"]
# our_fav_nnumbers = my_fav_numbers+friend_fav_numbers
# print(our_fav_nnumbers)
# num = 20
# for i in range (num+1):
#     print([i])
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(3)
# print(basket)
# print(basket)
# # basket.append("kiwi")
# print(basket)
# basket[0] = "apples"
# print(basket)
# basket.clear()
# print(basket)

print(basket.count("apples"))
# a = [*"realpython"]
# print(a)
# birthday = input("Enter your date of birth: ",)
# birthday_list = birthday.split("/")
# print("Day: ",birthday_list[0])
# print("Month: ", birthday_list[1])
# print("Year: ", birthday_list[2])
#
# word = "word"
# list_of_letters = list(word):
# print(list_of_letters)
# #
# def triangle():
#     height = input("Please enter height of triangle: ")
#     base = input("Please enter base of triangle: ")
#     height = int(height)
#     base = int(base)
#     area = (height*base)/2
#     print("The area of the triangle is",area)
# triangle()

# import time
#
# def happy_birthday(name):
#  name = name.capitalize()
# for x in range(3):
#  print(" "*23, "i  i  i")
# time.sleep(1)
# print(" " *21 , " ___ _ i_" "!")
# time.sleep(1)
# print(" "*20, "|"," "*12, "|" )
# time.sleep(1)
# print(" "*20, "|",""*12, "|" )
# time.sleep(1)
# print(" "*16, "~"*10)
# time.sleep(1)
# print(" "*20, "|",""*20, "|" )
# time.sleep(1)
# print(" "*20, "|",""*12, "|" )
# time.sleep(1)
# for x in range(3):
#  print(" "*3,"|")
#
# happy_birthday("gary")
# import datetime

# birthday = input('Enter your birthday in dd/mm/yyyy format')
# day, month, year = list(map(int, birthday.split("/")))
# birthdate = datetime.date(year, month, day)
#
# print(f"Birthday is on {birthdate.strftime('%d/%m/%Y')}")

# mixed_type = ('C',0,0,'K','I','E')
#
# for i in mixed_type:
#     print(i,":",type(i))

# lst = [1,2,3,4,5,6,7]
# for i in range(len(lst)) :
#  if (i % 2 == 0):
#   print(i)

# nl=[]
# for x in range(150, 200):
#    if x%7==0 and x%5==0:
#     nl.append(str(x))
# print (','.join(nl))

# n = 1500
# for i in range(1500,2500):
#     if(i%7 ==0 and i%5==0):
#         print(i)
# favorite_fruits = input("enter favorite fruits")
# fruit = []
# fruit = favorite_fruits.split(",")
# for i in favorite_fruits:
#
#     print(i)
# favorite_fruits.split()
# print(fruit)
# party_size = input("How many people are in your dinner party tonight? ")
# party_size = int(party_size)
#
# if party_size > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready.")
# number = input("Give me a number, please: ")
# number = int(number)
#
# if number % 10 == 0:
#     print(str(number) + " is a multiple of 10.")
# else:
#     print(str(number) + " is not a multiple of 10.")
# # sample_dict = {
# #    "class":{
# #       "student":{
# #          "name":"Mike",
# #          "marks":{
# #             "physics":70,
# #             "history":80
# #          }
# #       }
# #    }
# # }
# # print(sample_dict["class"]['student']['marks'])
# #
# # rick_dict = {
# #     'first_name':'Rick',
# #     'last_name':'Sanchez'
# # }
# # # for key in rick_dict:
# # #     print(key)
# # #     rick_dict["first_name"] = "james"
# # #     print(rick_dict)
# # # rick_dict['first_name'] = [rick_dict['first_name'], "bob"]
# # print(rick_dict)
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# del sample_dict['name']
# del sample_dict['salary']
#
# print(sample_dict)
# key_to_remove = ["name","salary"]
# for key in key_to_remove:
#  del sample_dict[key]
# print(sample_dict)
# for numbers in range(2,100):
#     print(numbers)

# name = input("enter a name: ")
# use_1 = len(name)
# name = "adisu"
# if len(name)==use_1:
#      print("wow its cool")
# elif len(name)!=use_1:
#      print("no ooh its not good")

# number_1 = int(input("ask user numbers is even or odd"))
# if number_1%2 == 0:
#      print("number is even")
# elif number_1%2 == 1:
#      print("number is odd")
#
# output = ("hello owlrd"
#           "hello world"
#           "hello world"
#           "hello world"
#           "hello world"
#         "hello world"
#           "I love python"
#        "I love python"
#        "I love python"
#        "I love python")
# print(output, end=",")

# name_month = input("user to input a month")
# if name_month in ("march""april" "may"):
#         print(spring)
# if name_month in ("june,july,August"):
#         print("summer")
# if name_month in ("semptember,octomber,november"):
#            print("Autumn")
# if name_month  in ("december,january,february"):
#           print("winter")
#
# elif name_month in ("quagme"):
#          print("extra season")

# print(3<-3<9)
# print(3==3==3)
# print(bool(0))
# print(bool(5=="5"))
# print(bool(4==4)==bool("4"==("4")))
# # print(bool(bool(none)))
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)
# my_text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elitqw,"
# "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
# "Ut enim ad minim veniam, quis nostrud exercitation ullamco"
# "laboris nisi ut aliquip ex ea commodo consequat"
# "Duis aute irure dolor reprehenderit voluptate velit"
# "esse cillum dolore eu fugiat nulla pariatur"
# "Excepteur sint occaecat cupidatat non proident,"
# "sunt culpa qui officia deserunt mollit anim id est laborum")
#
# print(len(my_text))
# word_list = input("enter longest sentences")
# def find_longest_word(word_list):
#     longest_word =  max(word_list, key=len)
#     return longest_word
# print("congrajualtion")
# num = 1
# for n in range (1,20):
#     if n<=20:
#         print(n)
#         # pizza = input("enter pizza topping")
#         # pizza += input()
#         # while true: 'quit'
#         # if topping != "quit":
#         #     print("i ll add" + topping + "your....")
#         # else:
#         #     break
# person = int(input("theater charges different ticket"))
# for age in range(person):
# #     if age < 13:
# #         print("ticket is free")
# #     if age  ==3|12:
# #         print("the ticket is $10")
# #     if age > 13:
# #         print("the ticket is $15")

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print("I'm working on your " + current_sandwich + " sandwich.")
#     finished_sandwiches.append(current_sandwich)
#
# print("\n")
# for sandwich in finished_sandwiches:
#     print("I made a " + sandwich + " sandwich.")
a = "numbers"
b = "letters"
print(a,b , end="")

# num1 = 10
# num2 = 14
# num3 = 12
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
#
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
#
# print("The largest number is", largest)

# names = (input("ask user for their name"))
list_integers = [2,3,5,6,7,98,86,23,45,78]
list(list_integers)
print(list_integers)
list_integers.sort()
print(list_integers)
list_integers.reverse()
print(list_integers)
sum = sum(list_integers)
print(sum)
print(list(range(1, 20, 3)))
for item in enumerate('abcd'):
    print(item)
key = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for key in zip( key, values):
    print(key)
