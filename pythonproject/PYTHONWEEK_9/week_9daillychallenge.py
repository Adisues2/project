
#  passing by value
# def sub(num: int):
# 	num -= 3

# 	return num

# x = 5
# print(x)

# x = sub(x)

# print(x)


# # pass by reference
# def add_to_dict(my_dict):
# 	my_dict['key1'] = 'val1'

# d = {}
# print(d)
# add_to_dict(d)
# print(d)

# recursive example

#  def print_until_10_rec(num):
#    # Base Case (when to stop)
#    if num > 10:
#       return

#    # Work toward Base Case
#    print(num)

#    # Recursive Call (call ourselves)
#    print_until_10_rec(num + 1)
 # def get_sum(*arg):
    #    result = 0
    #    for i in arg:
    #     result += i
    #     return result
    # print(get_sum(1,8))
    # print(get_sum(4,3))
    
    
class Node:
    def __init__(self,value ,left = None,right =None):
         self.left = left
         self.right = right
         self.value =value
         
    def get_left(self):
        return self.left*self.value
    def get_right(self):
        return self.right
    def set_left(self,node):
         self.left = left
    def set_right(self,node):
            self.right = right    
    
    def get_value(self,value):
        return self.value 
    def set_value(self,value):
        self.value= value
    
    def __str__(self):
        return f"the node with value {self.value}\n:None\nright:None\n{'-'*20}" 
    
      
    def add_node(self,node):
     
     
        if node.value < self.value:
          if not self.left :
              self.left = node
              self.add_node(node)
        else:
            if not self.right:
                self.right = node
  
        
             
root = Node(8)
print(root)
node_10 = Node(10)
root.add_node(node_10)

node_3 = Node(3)
root.add_node(node_3)
