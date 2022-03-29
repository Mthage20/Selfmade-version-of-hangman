import random
from english_words import english_words_lower_alpha_set

def play_game(secret_word):
        word_progression = '_' * len(secret_word)
        word_found = False
        guessed_chars = []
        lives = 6

        while word_found is not True and lives != 0:
            print(word_progression)
            guess = input('\nEnter your guess: ').lower()

            if len(guess) == 1 and guess.isalpha:
                if guess in guessed_chars:
                    print("You've already guessed that letter, try again!")
                elif guess not in secret_word:
                    lives -= 1
                    print(guess, 'is unfortunately not in the word :(')
                else:
                    print('Good guess! ', guess, 'is in the word!')
                    guessed_chars.append(guess)
                    temp_word_progression = list(word_progression)
                    indices = [i for i, letter in enumerate(
                        secret_word) if letter == guess]
                    for index in indices:
                        temp_word_progression[index] = guess
                        word_progression = "".join(temp_word_progression)

            elif len(guess) == len(secret_word) and guess.isalpha:
                if guess == secret_word:
                    word_found = True
                else:
                    lives -= 1
                    print(guess, 'is unfortunately not the word :(')

            else:
                print(
                    'You can only guess 1 character or a whole word with the length of the secret word')

            if lives == 0:
                print('Game over :(')
            if word_found or '_' not in word_progression:
                print('\nCongratulations! You won! :D')


def get_word(word_list):
    word_choice = input('Enter your choice: \n\n- r = random english word \n\n- t = typed word\n\n\n')

    if word_choice == 'r': secret_word = random.choice(word_list).lower()
    
    elif word_choice == 't': secret_word = input('Enter the word you want to use for hangman: ').lower()

    elif word_choice == 'q': quit()
    
    else: print('Incorrect input')

    return secret_word


def main():
    word_list = []  

    for x in english_words_lower_alpha_set: # Each element in the set of english words gets appended to the word_list
        word_list.append(x)
    
    secret_word = get_word(word_list)
    play_game(secret_word)


if __name__ == '__main__':
    main()

    