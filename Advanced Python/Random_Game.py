import random


def run_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print("Correct!")
            return True
    else:
        print("Hey! Only a number from 1 to 10!")
        return False


answer = random.randint(1, 10)
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number from 1 to 10: '))
            if (run_game(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
