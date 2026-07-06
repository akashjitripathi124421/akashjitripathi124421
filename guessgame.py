import random

number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: 🙌  "))
count = 1

while guess != number:
    guess = int(input("Guess again: 🙌  "))
    count += 1
    if guess < number:
        print("Too low! 😒")
    elif guess > number:
        print("Too high! 😒")
    else:
        print("Congratulations! You guessed the number.😍 ")
print(f"It took you {count} guesses.")