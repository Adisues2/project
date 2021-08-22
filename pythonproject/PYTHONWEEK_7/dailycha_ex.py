numerator  = int(input("numerator number"))
denumerator  = int(input("numerator number"))

# compute = numerator/denumerator
try:
    compute = numerator/denumerator
    print(compute)
except:
    print('there is no zero deivision')

finally:
    print('computed')
# words = input("enter words comma separated and sorted them alphabetcally").split(',')
# word = []
# for word in words:  
#     print(sorted(list(word)))

def calc():
    	try:
	        5/0
	except ZeroDivisionError:
            print("can't divide by zero")

calc()

