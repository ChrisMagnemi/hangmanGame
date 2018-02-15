#sidewaysHangmanGame.py
from random import randint

print(" \n-----------------Sideways Hangman wahoo!!!-------------------")
print(">--|--[O-:]   <- this is your stick man...dont kill him")

print("""
\t The game is hangman.
But some of the words are made up...
Sooooo.... good luck! \n""")


def random_word():
    words = ["super", "duper", "hangman", "flurbo", "plumbus", "gym"]
    words += ["kick", "flingo", "jump", "queen", "mattress", "yolk", "gratitude", "confidence"]
    words += ["jewish", "leaf", "leaves", "leaflet", "paper", "rolls", "jelly", "eggs", "zoo" ]
    words += ["zebra", "horse", "debugging", "code", "city"]
    return words[randint(0, len(words)-1)]

def initial_spaces(goal_word):
    output = []
    [output.append('_ ') for i in goal_word]
    # output = ('_ '* len(goal_word))
    return output

def print_game_status(spaces_as_list, stickman):
    # print(f"Your goal is to get this word:  {goal_word}")
    spaces = ''.join(spaces_as_list)
    print(f"\nHere is your progress: {spaces}")
    print(f"Here is your stickman: {stickman} \n")

def handle_guess(guess, letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs):
    guess = guess.lower()
    if len(guess) > 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
        print("Just one letter please!!")
        guess = input("Guess 1 letter: ")
        return handle_guess(guess, letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs)
    elif guess in letters_guessed:
        print(f"You already guessed '{guess}' !!")
        guess = input("Guess a NEW letter: ")
        return handle_guess(guess, letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs)
    else:
        letters_guessed.append(guess)
        if guess in goal_word:
            print("Nice Guess!")
            for i in range(len(goal_word)):
                if goal_word[i] == guess:
                    spaces_as_list[i] = guess
        else:
            print("Bad Guess :(")
            # stickman += "X"
            num_wrongs += 1
        return letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs

def update_stickman(stickman, num_wrong_guess):
    original_stickman_array = ['>','-','-','|','-','-','[','O','-',':',']']
    for i in range(num_wrong_guess):
        original_stickman_array[i] = 'X'
    return ''.join(original_stickman_array)


def main():
    goal_word = random_word()
    spaces_as_list = initial_spaces(goal_word)
    num_wrongs = 0
    letters_guessed = []
    original_stickman_array = ['>','-','-','|','-','-','[','O','-',':',']']
    stickman = ">--|--[O-:]"
    print_game_status(spaces_as_list, stickman)
    while goal_word != ''.join(spaces_as_list):
        guess = input("Guess a letter: ")
        letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs = handle_guess(guess, letters_guessed, goal_word, spaces_as_list, stickman, num_wrongs)
        stickman = update_stickman(stickman, num_wrongs)
        print_game_status(spaces_as_list, stickman)
        if stickman == 'XXXXXXXXXXX':
            print("You killed the stickman! You Lose!")
            print(f"Your word was {goal_word}")
            exit(0)
    print("You got the word correct and saved the stickman!!")

main()
