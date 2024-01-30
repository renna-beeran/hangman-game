import string
import random


def is_word_guessed(secret_word, letters_guessed):
  flag = True
  for i in secret_word:
    if i not in letters_guessed:
      flag = False
      break

  return flag

def get_guessed_word(secret_word, letters_guessed):
  nlist = [x if x in letters_guessed else '_ ' for x in secret_word]
  return ''.join(nlist)

def get_available_letters(letters_guessed):

    available = string.ascii_lowercase
    for i in letters_guessed:
      available = available.replace(i,'')

    return available

def hangman(secret_word):
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(' '+'-'*35)

    guesses_remaining = 6
    letters_guessed = []

    while True:
      print(f'You have {guesses_remaining} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')

      char = input("Please guess a letter: ")
      if char in letters_guessed:
        print('You\'ve already guessed that letter')
        print(' '+'-'*35)
        continue
      elif char.isalpha() == False:
        print('That is not a valid letter.')
        print(' '+'-'*35)
        continue
      elif len(char)!=1:
        print("Please enter 1 character")
        print(' '+'-'*35)
        continue
      letters_guessed.append(char.lower())

      if char in secret_word:
        print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}')
      else:
        print(f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
        if char in 'aeiou':
          guesses_remaining -= 2
        else:
          guesses_remaining -= 1

      print(' '+'-'*35)

      if is_word_guessed(secret_word, letters_guessed):
        total = guesses_remaining * len(set(secret_word))
        print(f'Congratulations, you won!\nYour total score for this game is: {total}\n')
        break

      if guesses_remaining == 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}\n')
        break
    
words = ['army', 'beautiful', 'sorry', 'became', 'if', 'actually', 'beside', 'between', 'come',' eye', 'five', 'fur', 'imposter', 'problem', 'revenge', 'few', 'circle', 'district', 'trade', 'quota', 'stop', 'depressed', 'disorder', 'dentist', 'square', 'charger', 'color','stick']

random_word = random.choice(words)

hangman(random_word)