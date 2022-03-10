
available_exits = ["north", "south", "east", "west"]

chosen_exits = ""

while chosen_exits not in available_exits:
    chosen_exits = input("Please choose a direction: ")

print("aren't you glad you got out of there")