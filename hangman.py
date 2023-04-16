import random

word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


chosen_word = random.choice(word_list)
print(chosen_word)

print(stages[6])
display = []
for letter in chosen_word:
    display.append("_")

print(display)
lives = 6
while "_" in display or lives > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You have {lives} lives left")
        if lives == 0:
            print("You lose")
            break
    if "_" not in display:
        print("You win")
        break

