
# class BankAccount:
#     def __init__(self,balance,username,password,authenticated:False):
#         self.username = username
#         self.password =password
#         self.authenticated =False
#         self.balance = []
#     def authencticated(self,username,password):
#         if username == password:
#             # return True
#             print("login successfull")
#         else:
#             # return False
#             print("invalid")
#     def deposit(self,amount):
#         # self.balance.append("deposit")
#         if amount<0:
#             print(f"insuffe ballance you need deposit more money")
#         else:
#             self.balance.append(amount)
#             print (f'your current balance is :{amount}')
#     def withdraw(self,amount):
#         if amount<30:
#             print(f" insufficient balance you cant withdraw")
#         else:
#             # return self.balance
#             print(f"possible to withdraw")
            
                     
# class MinimBalanceAmount(BankAccount):
    
#     def __init__(self, minimum_balance =0):
#         self.minimum_balance = minimum_balance
#         super().__init__(self)
#     def withdraw(self,minimum_balance):
#         if self.balance >minimum_balance:
#             print(f"allow the user to withdraw money")
#         else:
#             print("insufficient minimum_balance")
       
# account = BankAccount(100,"smith","smith",False)
# account.authencticated("smith","smith")
# account.deposit(100)
# account.withdraw(50)



import random

number = random.randint(1,10)

player_game = input('hello, whats your name')
number_of_guess = 0
print('okay' +  player_game + 'i am guessing a number between 1 and 10')


while number_of_guess <5:

    guess = int(input())
    number_of_guess+=1
    if guess < number:
        print('your guess is low')
    if guess>number:
        print('your guess is to high')
    if guess == number:
        print("you guessed the numberin" + str(number_of_guess) + 'tries')
    else:
        print('you did not guess the number ,the number was ' + str(number))

            
            
        
