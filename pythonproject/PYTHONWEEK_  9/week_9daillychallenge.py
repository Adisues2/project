class Node:
    def __init__(self,left,right,value):
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
        
    def add_node(self,node):
        return self.get_right
    def search(self,value):
       return  self.value
   
    def get_sum(*arg):
       result =5
       for i in arg:
        result+=i
        return result
    print(get_sum(1,3,4))
    print(get_sum(4,6,8))