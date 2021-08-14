
#  # print("hello world"
#  #             "hello world"
#  #            "hello world"
#  #            "hello world"
#  #              )
#  # print(5<3)
# # print(3==3)
# # print(3=="3")
# # print("3">3)
# # print("Hello" == "hello")
# # computer_brand = "lenovo"
# # print(f"i have a {computer_brand} computer")
# # name = "adisu"
# # age = 29
# # shoe_size = 40
# # info = f"my name is {name} and i m {age} years old ,also i wear {shoe_size} number shoe"
# # print(info)
# #  a =4
# # b = 6
# # if a>b:
# #
# #  print("hello world")
# # if a<b:
# #  print("cool")
# # input_string = input("enter string character:")
# # if len(input_string)<10:
# #         print("string noit long enough")
# # elif len(input_string)>10:
# #     print("not enough")
# #     str_array = []
# #     str_array = input_string
# #     print('first char is ' + str_array[0]+ 'and last char' + " "+ str_array[len(str_array)-1])
# number_1 = int(input("ask user numbers is even or odd"))
# if number_1%2 == 0:
#      print("number is even")
# elif number_1%2 == 1:
#      print("number is odd")

# name = input("enter a name: ")
# use_1 = len(name)
# name = "adisu"
# if len(name)==use_1:
#      print("wow its cool")
# elif len(name)!=use_1:
#      print("no ooh its not good")

# height = int(input("ask a user height in inches:"))
# if height>145:
#         print("they are tall enough to ride")
# elif height<145:
#          print("they need to grow some more to ride")
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

# print(len(my_text))
# word_list = input("enter longest sentences")
# def find_longest_word(word_list):
#     longest_word =  max(word_list, key=len)
#     return longest_word
# print("congrajualtion")
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
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

# print(basket.count("apples"))
# num = 1
# for n in range (1,20):
#     if n<=20:
#         print(n)
# my_fav_numbers = ["2","4","6","8","12","14","16"]
# my_fav_numbers.append("20", )
# print(my_fav_numbers)
# my_fav_numbers.remove("20")
# print(my_fav_numbers)
# friend_fav_numbers = ["3", "5"]
# our_fav_nnumbers = my_fav_numbers+friend_fav_numbers
# print(our_fav_nnumbers)
# n = 1500
# for i in range(1500,2500):
#     if(i%7 ==0 and i%5==0):
#         print(i)
# favorite_fruits = input("enter favorite fruits")
# fruit = []
# fruit = favorite_fruits.split(",")
# for i in favorite_fruits:

#     print(i)
# person  = int(input("theater charges different ticket"))
# for age in range (person):
#     if age<13:
#         print("ticket is free")
# if age<3:
#         print("the ticket is $10")
# if age>13:
#         print("the ticket is $15")

# a = "numbers"
# b = "letters"
# print(a,b , end="")
# num1 = 10
# num2 = 14
# num3 = 12
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)
list_integers = [2,3,5,6,7,98,86,23,45,78]
list(list_integers)
print(list_integers)
list_integers.sort()
print(list_integers)
list_integers.reverse()
print(list_integers)
sum = sum(list_integers)
print(sum)
key = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for key in zip( key, values):
    print(key)