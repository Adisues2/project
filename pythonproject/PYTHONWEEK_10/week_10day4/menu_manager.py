
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
