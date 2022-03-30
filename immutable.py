# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# print()
#
# result = False
# another_result = result
# print(id(result))
# print(id(another_result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

print()

result += "ish"
print(id(result))