#Jack Lesemann jwl4vg
import random

number = int(input("What should the number be? "))

if number < 1:
    number = random.randrange(1, 101)

guess_limit = int(input("How many guesses? "))

guess_count = 0
guess = 0

while guess_count < guess_limit and guess != number:
    guess = int(input("Guess a number: "))

    guess_count += 1

    if guess < number:
        print("The number is higher than that.")
    elif guess > number:
        print("The number is lower than that.")
    elif guess == number:
        print("You win!")

print("You lose; the number was ", number, ".")


