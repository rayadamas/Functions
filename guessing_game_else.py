import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid input.".format(temp))

highest = 100
answer = random.randint(1, highest)
guess = 0
print(answer) # TODO: remove after testing
print("Please guess a number between 1 & {}: ".format(highest))

# Program with a While loop Challenge
while guess != answer:
    # print("Please guess a number between 1 & {}: ".format(highest))
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be > than answer
            print("Please guess lower")