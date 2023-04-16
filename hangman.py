import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
print(stages[6])
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

print(f"{' '.join(display)}")

lives = 6
while "_" in display or lives > 0:
    guess = input("\nGuess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        print(f"You have {lives} lives left")
        if lives == 0:
            print("You lose!")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win")
        break

print(f"The word was {chosen_word}")

