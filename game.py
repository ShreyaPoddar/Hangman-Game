import re
import random
import string
def hangman():
    name=input('Enter your name')
    print("Welcome to the hangman game {0}".format(name))
    attempts_remaining=num_of_attempts()
    min_word_length=min_wordlength()
    print("Selecting word")
    word=get_word(min_word_length)
    boolean = [letter not in string.ascii_lowercase for letter in word]
    remaining_letters = set(string.ascii_lowercase)
    wrong_letters = []
    word_solved = False
    while attempts_remaining > 0 and not word_solved:
        print('Word: {0}'.format(display_word(word,boolean)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(','.join(wrong_letters)))
        next_letter = get_next_letter(remaining_letters)
        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    boolean[i] = True
        else:
            print('{0} is NOT in the word!'.format(next_letter))

        attempts_remaining -= 1
        wrong_letters.append(next_letter)
        if False not in boolean:
            word_solved = True
    print('\nThe word is {0}'.format(word))
    if word_solved:
        print('Hats off!You won!')
    else:
        print('Boo,you lost :(')
    try_again = input('\nWould you like to try again? [y/n] ')
    return try_again == 'y'


def get_word(length):
    words1 = []
    with open("word_list.txt",'r') as f:
        for word in f:
            if ((re.search("[@_!#$%^&*()<>?/\|}{~:]",word)) !=None):
                continue
            if len(word) < length:
                continue
            if len(word.strip().lower()) == length:
                words1.append(word.strip().lower())
    return random.choice(words1)

def num_of_attempts():
    while True:
        attempts=input('How many attempts do you want between 1-25')
        try:
            attempts = int(attempts)
            if 1 <= attempts <= 25:
                return attempts
            else:
                print('{0} is not between 1 and 25'.format(attempts))
        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(attempts))

def min_wordlength():
    while True:
        min_length=input('Enter the length of word between 4-10')
        try:
            min_length=int(min_length)
            if 4 <= min_length <= 10:
                return min_length
            else:
                print('{0} is not between 1 and 25'.format(min_length))
                continue
        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(min_length))

def display_word(word,boolean):
    displayed_word=''
    if(len(word)!=len(boolean)):
        raise ValueError('Length of word and boolean doesnt match')
    for i,j in enumerate(word):
        if(boolean[i]==True):
            displayed_word=displayed_word+j
        else:
            displayed_word = displayed_word + '_'
    return displayed_word.strip()

def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in string.ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

if __name__ == '__main__':
    while hangman():
        print()
