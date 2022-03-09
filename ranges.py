for i in range(1, 20):
    print("i is now {}".format(i))

# provide start value or not
print("*" * 15)

for i in range(5):
    print("i is now {}".format(i))

print("*" * 20)

for i in range(10, 0, -2):
    print("i is now {}".format(i))

print("*" * 20)

age = int(input("How old are you? "))

if age in range(16, 60):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("*" * 25)
# Challenge
# write a program that prints numbers from 0 to 100 that are divisible by 7

# This solution uses a slice
for i in range(101)[::7]:
    print(i)

print("*" * 25)

for i in range(0, 101, 7):
    print("i now is {}".format(i))