import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())


if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Guess a bit higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guess it")
    else:
        print("Sorry, you have not guessed the correct answer")