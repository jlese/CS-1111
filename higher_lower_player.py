#Jack Lesemann jwl4vg

print("Think of any number between 1 and 100 and I'll guess it. ")

guess_num = int(input("How many guesses do I get? "))

low = 1
high = 100

answer = None

for i in range(guess_num):
    guess = (low + high) // 2

    response = input("Is the number higher, lower, or the same as " + str(guess) + "? ")

    if response == "higher":
        low = guess
        if high - low == 1:
            print("Wait; how can it be both higher and lower than ", low, " and ", high)
            exit()
    elif response == "lower":
        high = guess
        if high - low == 1:
            print("Wait; how can it be both higher and lower than ", low, " and ", high)
            exit()
    elif response == "same":
        answer = guess
        break

if answer is None:
    answer = int(input("I lost; what was the answer? "))
    if low < answer < high:
        print("Well played.")
    else:
        print("That can't be, you said it was " + response + " than ", guess)
else:
    print("I win!")


