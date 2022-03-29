from english_words import english_words_lower_alpha_set
import random

if __name__ == '__main__':

    # Declare word_list to be a list
    word_list = []

    # For each x (str) in the set append it to word_list
    for x in english_words_lower_alpha_set:
        word_list.append(x)

    Word_choice = input('Enter your choice r = random english word, t = typed word\n')

    if Word_choice == 'r':
        word = random.choice(word_list)

        for i in word:
            print('_', end='')  # Print amount of _ equal to the amount of letters in the word without newline

    elif Word_choice == 't':
        word = input('Enter the word you want to use for hangman: ')

        for i in word:
            print('_', end='')  # Print amount of _ equal to the amount of letters in the word without newline

    elif Word_choice == 'q':
        quit()

    else:
        print('Incorrect input, either type r, t or q')

