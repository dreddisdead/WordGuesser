import time 
from random import randint
 
# In this simple game you will be given a word at random with portions blanked out. 
# You must guess the correct word to move on to the next word. Once you've guess 
# all words, you win! Otherwise, if you make 3 incorrect guesses it's game over. 

def read_words_from_file(filename):
    # pulls words from given file and returns them as a list
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        
    return words
# use above function to get the words from words.txt file
words = read_words_from_file('words.txt')

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
  global incorrect_attempts
  global words
  global chosen_word
  while True:
    user_answer = input('Guess the word:\n')
    correct_answer = chosen_word
    if user_answer == correct_answer:
      print('Correct!')
      words.remove(correct_answer)# remove correct word from list
      score += 1
      print(f'Current score is: {score}') # display current score
      break
      
    else:
      print('Not quite.')
      incorrect_attempts += 1
      if incorrect_attempts == 3:
        print('Game Over! No more attempts left.')
        score = 0
        incorrect_attempts = 0
        return False
  return True
  
while True:
  if not display_partial_word():
    break
  if not check_answer():
    break
    


