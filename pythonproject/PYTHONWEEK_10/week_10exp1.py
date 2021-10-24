import operators
from operators import addoperator
from operators import addoperator as add
import operators as mn
import random
import string,random
print(addoperator(2,4))
print(add(3,5))
print(mn)
# ex.2
value = random.randint(1,100)
print(value)
def num_random(a,b):
    print(random.randint(a,b))
    
if value == num_random:
    print('success message to the user')
else:
    print("dont")
num_random(1,100)
# 3x.3
input1 = input("enter random string of length")

length= len(input1)
print(random.sample(string.ascii_uppercase,length))
print(random.sample(string.ascii_lowercase,length))
print(''.join(random.sample(string.ascii_uppercase+string.ascii_lowercase,length)))

