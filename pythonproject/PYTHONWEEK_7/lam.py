# l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
# s = l2.count(4)
# print(s)
# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# for key ,value in d.items():
#  print(f"the key {key}   and the value {value}" )


myList = [1, 2, 3]
myListMultipliedWith2 = map(lambda n : n*2, myList)

print(list(myListMultipliedWith2))

myList = [10, 25, 17, 9, 30, -5]
myList3 =filter(lambda n : n%5 ==0 ,myList)
print(list(myList3))
