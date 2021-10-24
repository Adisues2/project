
import random


def get_words_from_file():
	with open("text.txt", "r") as file:
		return file.read().splitlines()


def  get_random_sentence(words, sentence_length):
	random_sentence = []

	for i in range(sentence_length):
		random_word = random.choice(words)
		random_sentence.append(random_word)

	return ' '.join(random_sentence)


def main():
	words = get_words_from_file()
	sentence_length = int(input('sentence length: '))
	random_sentence = get_random_sentence(words, sentence_length)

	print(random_sentence)


if __name__ == "__main__":
	main()