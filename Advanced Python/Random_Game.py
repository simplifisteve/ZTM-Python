from random import randint
import sys

sys.argv

# generate a number using lower and upper bounds
lower = int(sys.argv[1])
upper = int(sys.argv[2])
answer = randint(lower, upper)
chances = upper - 1
msg = "Sorry, you have ran out of chances!"

while chances > 0:
    try:
        guess = int(input(f"Guess a number from {lower} to {upper}: "))
        if guess == answer:
            print("You won!")
            break
        elif guess > upper or guess < lower:
            print(
                f"Only number from {lower} to {upper}! You have {chances} chances left!")
            chances -= 1
            continue
        elif guess > answer:
            print(f"Lower! You have {chances} chances left!")
            chances -= 1
        elif guess < answer:
            print(f"Higher! You have {chances} chances left!")
            chances -= 1
    except ValueError:
        print("Please enter a number!")
print(msg)
