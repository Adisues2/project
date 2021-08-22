# def checked (a,b,c):
#     print(a,b,c)

#     lst = ['item1','item2']
#     tp = {"item1",'item2' ,"items3"}
#     check(a =lst[0], b = lst[1] ,c= lst[3])
#     checked(lst)
#     checked(tp)

liSt =[1,2,3,4,  23,45,46]
sum = sum(liSt)
print(sum)
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
result = 0

for item in my_list:
	try:
		result += item
	except TypeError:
		continue

print(result)
list_count= (['a','a','t','o'],'a')

duplicates = []

for values in list_count:
	if list_count.count(values)>2:
				duplicates.append(values)
				print(duplicates)