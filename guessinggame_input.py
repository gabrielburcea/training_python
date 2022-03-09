answer = 5
print("Please guess number between 1 and 10: ")
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






# if guess != answer:
#     if guess < answer:
#         print("Guess a bit higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you've guess it")
#     else:
#         print("Sorry, you have not guessed the correct answer")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed it correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("You got it first time")

