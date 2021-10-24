from typing import Counter


def display_message(course):
    print(f"the coures is  {course}")

display_message('python')

def favorite_book(title):
 print(f"one of my favorite books is {title} in wonderland")
favorite_book('darwin')

def describe_city(country,city):
    print(f"{city} is in {country}")
describe_city('israel','jerusalem')

def make_shirt( brand, size):
    print(f"my tshirt is {size}  and {brand} ")

    
make_shirt('medium' , 'nike')
# import random
# for i in range (1,100):
#     print(random.random())
n_list = ["happy" , [1,2,3]]
print(n_list[1][1])

def insertion_sort(alist):
    for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)


# str = input('enter a character')
# count = {}
# for i in str:
    
#     if i in count:
#         count[i.lower()]=count[i.lower()]+1
#     else:
#         count[i.lower()]=1
#     print(count)
# 

string = "input"
character = " _"

for i in range(len(string)):
    string = string[:i] + character + string[i+1]
    