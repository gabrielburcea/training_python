import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after testing
guess = 0 #initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("You got it first time")
        break
    else:
        if guess < answer:
            print("Guess a bit higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
    #         guess = int(input())
    # if guess == answer:
    #     print("Well done, you've guess it")
    # else:
    #     print("Sorry, you have not guessed the correct answer")
