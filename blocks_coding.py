#Check the indentation

#for i in range(1, 13):
#   print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2 , i ** 3))
#   print("*" * 40)

name = input("Please input you name")
age = int(input("How old are you, {0}?".format(name)))

if age > 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please comeback in {} years".format(18 - age))

print()

if age < 18:
    print("Please comeback in {} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")