import random


def get_integer(prompt):
    """
    Guessing Game

    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user, until a valid 'int' is entered.


    :param prompt: The string the user will see, when
        they're prompted to enter the value.
    :return:    The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid input.".format(temp))


# print(input.__doc__) #Functions not being called, but instead we're referring to their Attributes
# print('-' * 80)
# print(get_integer.__doc__)
# print('-' * 80)

help(get_integer)

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
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guess correctly")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, bih you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, bih you was mf'in right!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("YOu got it first try!")

# A block can include further if & else blocks within it
# When testing for equality, we can't use a single `=`(used for assigning values to variables
# We must use `==`

# Using Conditional Operators

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be > than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")
# else:
#     print("You got it first try!")

# Challenge: change 1st line of code to `if guess == answer:` and output the same results

# if guess == answer:
#     print("You got it first try!")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be > than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")

# Binary Search

# Table
# 1-10, 1 = low, 10 = high, 5 = mid, the answer is 7


# low + (high - low) // 2

# 1 + (10 - 1) // 2
# Our first guess = 5, meaning the answer is now btwn 6 - 10
# Now our formula is 6 + (10 - 6) // 2 = 8 as second guess

# Now the answer must be btwn 6 - 7
# 6 + (7 - 6) // 2 = 6.5 rounded to 6 as third guess

# Now our formula is 7 + (7 - 7) // 2 = 7
