shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

print()

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")

print()
b.append("cream")
print(c)
print(d)


