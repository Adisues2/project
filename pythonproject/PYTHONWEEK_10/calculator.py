import operator
from operators import addoperator, dividedoperator 

print(addoperator(3,5))
print(dividedoperator(8,2))

from operators import  addoperator as add,dividedoperator as div

print(add(4,6))
print(div(6,3))