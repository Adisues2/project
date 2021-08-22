n = 10
for i in range(1,6):
    print(' '*n, end='')
    print('*'*(i))
    n-=1

n = 10
for i in range(1,6,2):
    print(' '*n, end='')
    print('*'*(i))
    n-=1


    my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)

sum = sum(my_list)
print(sum)
count= 0
string = 'welcome thankyou'
for i in  string:
            if (i.isspace()):
                count=count+1
            print('space',count)
    
list = ([0,1,3,50])
bG_N= max(list)
print(bG_N)
list_count= (['a','a','t','o'],'a')
count = list_count[0].count('a')
print('this is a count',count)
duplicates = []


for values in list_count:
    if list_count[0].count(values)>1:
        duplicates.append(values)
        print(duplicates)

def calculate_upp(str):
    s = {"upper_case":0 , "lower_case":0}
    for u in str:
        if u.isupper():
            s['upper_case']+=1
        elif u.islower():
            s['lower_case']+=1
        else:
            pass
        print('stringof',str)
        print("string", s["upper_case"])
        print("string", s["lower_case"])
        calculate_upp('NetFlix')

this_mono= ([7,6,5,5,2,0])

print(this_mono)
mono =sorted(this_mono)
print(mono)
num = ([2,3,3,3])  
print(sorted(num))
n = ([7,6,5,5,2,0])
def arraySorted(n ):

    array = []

    if (n == 1 or n == 0):
        return 1
    if (array[n - 1] < array[n - 2]):
        return 0
    return arraySorted(array, n - 1);
print(n)

lst = [1,23,34]
str = ["banaana" ,"orange" ,"apple"]
one_list = lst+str
print(one_list)

# my_sum = ([1,5,4,2])
# sum_1 = sum(my_sum)
# print(sum_1)

def ispalindrome(s):
    rev = ''.join(reversed(s))
    if(s==rev):
        return True
        return False
s = 'john'
ans = ispalindrome(s)
if(ans):
    print('yes')
else:
    print('no')

weird= ([1,2,2,3,4,5])
for x in weird:
    if x%2 == 0:
        print('even',x)

arr = ['a','b', 'c']
arr.insert(2, 'd')
print(arr)

num = 4
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1,num + 1):
#     factorial = factorial*i
# print("The factorial of",num,"is",factorial)

# dict_avg = {'a': 1,'b':2,'c':8,'d': 1}

# values = dict_avg.values()
# print(values)
# length = (len(dict_avg))
# print(length)
# total = (sum(dict_avg.values()))
# print(total)
# res_lst = [ item*5 if not item % 2 else item for item in lst ]
# words = input("enter words comma separated and sorted them alphabetcally")
# word = ""

# for word in words:  
#    word = words.split(',').sort()
# #    word.sort()
# print(word)
# words = input("Write a sequence of words separated by comas: ")
# words_list = words.split(",")
# words_list.sort()


# print(f"The sorted order is: {words_list}")
# items = input("Input comma separated sequence of words")
# words = [word for word in items.split(",")]
# print(",".join(sorted(len(words))))