
import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_to_guess = list('*'*len(word))
number_of_wrong_guessing = 0
while number_of_wrong_guessing < 5:
    try_letter = input(f"Try to guess the word {''.join(word_to_guess)}. Please, write a letter:")
    index = word.find(try_letter)
    if index != -1:
        if word_to_guess[index] != '*':
            index = word[index+1:].find(try_letter)
        word_to_guess[index] = try_letter
        print('correct')
        if ''.join(word_to_guess) == word:
            print('You are a winner')
            break
    else:
        print('Wrong guessing')
        number_of_wrong_guessing +=1
else:
    print('You lose')
