def get_word():
    import random
    f = open("countries-and-capitals.txt", "rt")
    lines = f.readlines()
    f.close()
    get_word = random.choice(lines)
    two_words = get_word.rstrip("\n").split("|")
    one_word = random.choice(two_words)
    print(one_word)
get_word()