greeting = "Hello"
#name = "Tim"
#print(greeting + name) #no space
name = "Bruce"
#if we want a space, we can add that too
print(greeting + ' ' + name) #it will give me a space

# other points in 4th section of the course
age = 24
print(age)

print(type(age))
print(type(greeting))

#age_in_words = "2 years"
#print(name + " is " + age + " years old") # here will get an error
#print(type(age))

# here we can add f before " is "
age_in_words = "2 years"
print(name + f" is {age} years old") # here will get an error
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7

print(f"Pi is approximatelly {pi:12.50f}")
