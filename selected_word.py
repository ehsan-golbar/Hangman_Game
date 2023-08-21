import random


def selecte_word(easy, medium, hard):
    selected_words = []
    if easy :
        with open('C:\\Users\\reza\\Desktop\\New folder (3)\\Hangman_Game\\Hangman_Game\\easy_word.txt') as f:
            easy_word = f.readlines()
        selected_words.extend(easy_word)
    # if medium :
    #     with open('medium_word.txt') as f:
    #         medium_word = f.readlines()
    #     selected_words.extend(medium_word)
    if hard :
        with open('C:\\Users\\reza\\Desktop\\New folder (3)\\Hangman_Game\\Hangman_Game\\hard_word.txt') as f:
            hard_word = f.readlines()
        selected_words.extend(hard_word)

    word = random.choice(selected_words)
    selected_words.remove(word)
    print(word)
    return word


