import random
import string

lives = 11

def get_random_word_from_file(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    get_word = random.choice(lines)
    two_words = get_word.rstrip("\n").split(" | ")
    word = two_words[0]
    return word

word = get_random_word_from_file("countries-and-capitals.txt")

abc = set(string.ascii_uppercase)

guessed_letters = set()

def print_lines(): 
    number_of_lines = len(word)  
    if ' ' in word:
        words = word.split(" ")    
        for i in range(len(words)):
            a = len(words[i])
            print('_ ' * a, ' ')
    elif '-' in word:
        words2 = word.split("-")
        print('_ ' * len(words2[0]),'-','_ ' * len(words2[1]))
    else:
        print('_ ' * number_of_lines)

while lives > 0:
    print(chr(27) + "[2J")
    print_lines()
    user_guess = input('Type in a letter: ').upper()
    if user_guess not in abc:
        user_guess = input('Type in a letter, please: ').upper()
    elif user_guess in guessed_letters:
        print('These are the letters you\'ve already guessed', guessed_letters)
        user_guess = input('You\'ve tried this one already. Type in a new one: ').upper()
        guessed_letters.add(user_guess)
    else:
        guessed_letters.add(user_guess)




def play():
    while lives > 0:
        print_lines()
#        get_guess()
        print(chr(27) + "[2J")              
        

#"escape sequence"


#play()    

#def reveal():


#def quit():

    
#def lives_decrease():


#def occurance():


#def win():


#def bye_bye():

#def play(word, lives):