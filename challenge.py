name = input("Please enter name: ")
age = int(input("How old are you? "))


if age >= 18 and age < 31:
    print("Welcome to Phi Phi island {}".format(name))
else:
    print("Please bear in mind {}, we do not accept your age group to Phi Phi island".format(name))
