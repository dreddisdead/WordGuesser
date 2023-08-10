import time 
from random import randint
 
# In this simple game you will be given a word at random with portions blanked out. 
# You must guess the correct word to move on to the next word. Once you've guess 
# all words, you win! Otherwise, if you make 3 incorrect guesses it's game over. 

# List of word files, ordered by difficulty
word_files = ['food.txt', 'candy.txt', 'animal.txt', 'soda.txt', 'car.txt', 'dessert.txt', 'country.txt'] # add more as needed
current_difficulty = 0

def read_words_from_file(filename):
    # pulls words from given file and returns them as a list
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        
    return words

def load_next_difficulty():
    global current_difficulty
    global words
    if current_difficulty < len(word_files):
        words = read_words_from_file(word_files[current_difficulty])
        current_difficulty += 1
    else:
        print('Congratulations, you have finished all levels!')
        return False
    return True

# read the high score from the file
def read_high_score(filename):
    try:
        with open(filename, 'r') as file:
            high_score = int(file.read())
    except FileNotFoundError:
        # if the file doesn't exist, return 0 as the default high score
        high_score = 0
    return high_score

# write the high score to the file
def write_high_score(filename, high_score):
    with open(filename, 'w') as file:
        file.write(str(high_score))
        
# initialize the high score variable from the file
high_score = read_high_score('high_score.txt')

# load the words for the first difficulty level
load_next_difficulty()

chosen_word = None
score = 0
incorrect_attempts = 0

def choose_word(list_of_words):
    # picks random word from list of words by generating index within list 
    if len(list_of_words) > 0:
        chosen_word_idx = randint(0, len(list_of_words) - 1)
        return chosen_word_idx
    else:
        return None


def replace_letters(word):
    # removes vowels from chosen word
    list_of_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    new_word = []
    for letter in word:
        # if letter is a vowel then replace it with a blank
        if letter in list_of_vowels:
            new_word.append('_')
        else:
            new_word.append(letter)

    return ''.join(new_word)# creates new string with replaced vowels

def display_partial_word():
    global chosen_word
    chosen_word_index = choose_word(words)
    if chosen_word_index is not None:
        chosen_word = words[chosen_word_index]
        print(replace_letters(chosen_word))
    else:
        print("***YOU WIN!***")
        return False
    return True


def check_answer():
    global score
    global high_score
    global incorrect_attempts
    global words
    global chosen_word
    while True:
        user_answer = input('Guess the word:\n')
        correct_answer = chosen_word
        if user_answer == correct_answer:
            print('Correct!')
            score += 1
            # update high score if current score is higher
            if score > high_score:               
                high_score = score
                write_high_score('high_score.txt', high_score)
                
            words.remove(correct_answer)# remove correct word from list           
            print(f'Current score is: {score}') # display current score
            break
      
        else:
            print('Not quite.')
            incorrect_attempts += 1
            if incorrect_attempts == 3:
                print('Game Over! No more attempts left.')
                print(f'***High score is: {high_score}***')
                score = 0
                incorrect_attempts = 0
                return False
    return True
  
while True:
    if not display_partial_word():
        break
    if not check_answer():
        break
    if len(words) == 0:
        print("You're doing great! Moving on to the next level...")
        if not load_next_difficulty():
            break

    


