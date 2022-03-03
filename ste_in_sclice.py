#                     1
#         012345678911234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  #NRE
print(parrot[0:6:3])  #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])