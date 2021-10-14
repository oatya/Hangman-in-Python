import random
import string
from types import DynamicClassAttribute

print ("Hello, let's play!")

hangman_graphics = ["_",
                    "__",
                    "__\n |",
                    "__\n |\n O",
                    "__\n |\n O\n |",
                    "__\n |\n O\n/|",
                    "__\n |\n O\n/|\ ",
                    "__\n |\n O\n/|\ \n/",
                    "__\n |\n O\n/|\ \n/ \ ",
                    ]


lives = 6

abc = set(string.ascii_uppercase)

guessed_letters = set()

def get_random_word_from_file(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    get_word = random.choice(lines)
    two_words = get_word.rstrip("\n").split(" | ")
    word = two_words[0]
    return word

word = get_random_word_from_file("countries-and-capitals.txt")


def user_guess(abc): 
    user_guess = input('Type in a letter: ').upper()
    if user_guess not in abc:
        user_guess = input('Type in a letter, please: ').upper()
    elif user_guess in guessed_letters:
        print('These are the letters you\'ve already guessed', guessed_letters)
        user_guess = input('You\'ve tried this one already. Type in a new one: ').upper()
        guessed_letters.add(user_guess)
    else:
        guessed_letters.add(user_guess)
    return user_guess


def print_lines(): 
    number_of_lines = len(word)  
    if ' ' in word:
        words = word.split(" ")
        for i in range(len(words)):
            a = len(words[i])
            print(' _ ' * a, ' ')
    elif ' - ' in word:
        words2 = word.split("-")
        print(' _ ' * len(words2[0]), ' - ', ' _ ' * len(words2[1]))
    else:
        print(' _ ' * number_of_lines)


def convert_str_to_list(str):
    wordList = []
    for char in str:
        wordList.append(char)
    return wordList

word_list = convert_str_to_list(word)

def get_under_score_list(list):
    created_list = []
    for item in list:
        if(item == ' '):
            created_list.append(' ')
        else:
            created_list.append('_')
    return created_list


def get_index(word_list_given, guess_letter):
    index_list = []
    for index in range(len(word_list_given)):
        if guess_letter.upper() == word_list_given[index].upper():
            index_list.append(index)
    return index_list


def exchange_displayed_list(index_list, word_list_given, displayed_list_given):
    for index in index_list:
        displayed_list_given[index] = word_list_given[index]
    return displayed_list_given


word_list = convert_str_to_list(word) 
displayed_list = get_under_score_list(word_list)
print(" ".join(displayed_list))

while list.count((displayed_list), "_") > 0 and lives !=0:
    guess = user_guess(abc)
    index_list = get_index(word_list, guess)
    displayed_list = exchange_displayed_list(index_list, word_list, displayed_list)
    if guess not in word:
        guessed_letters.add(user_guess)
        lives = lives - 1
    print(chr(27) + "[2J") 
    print(" ".join(displayed_list))
    if displayed_list.count("_") == 0:
        print("\Yay! You scored all letters!")
    if lives == 0:
        print("Game Over!")