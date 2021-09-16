class Phone:
   
    def __init__(self, phone_number,call_history,messages):
        self.messages = {}
        self.phon_number =phone_number
        self.call_history = []
    def call(self,other_phone):
        self.other_phone = other_phone
        
        print("hello whois that")
        self.call_history.append(other_phone)
    def show_call_history(self):
         return self.call_history
    # def messages(self):
    #     # return self.messages
    #     self.messages.append(self)           
        
    def send_message(self,key,value):
   
        self.messages.update({key:value})
       
    
calling = Phone("111","lastcall","10minutes ago")
calling.call("33")
calling.call("444")
print((calling.call("445")))
print((calling.call("440")))
print((calling.call("446")))
print((calling.call("442")))
print(calling.show_call_history())

calling.send_message("to 122","10minutes ago")
calling.send_message("from 111","40minutes ago")
calling.send_message("from 333 ","10minutes ago")
print(calling.messages)
