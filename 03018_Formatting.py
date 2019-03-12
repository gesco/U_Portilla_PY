print("This is a string {}".format("INSERTED"))
# This is a string INSERTED

print("The {2} {1} {0}".format("fox", "brown", "quick"))
# The quick brown fox

print("The {0} {0} {0}".format("fox", "brown", "quick"))
# The fox fox fox

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
# The quick brown fox

##########################################################
# Float formatting follows "{value:width.precision f}"
##########################################################
result = 100/777

print("The result was {}".format(result))
# The result was 0.1287001287001287

print("The result was {r:1.3f}".format(r = result))
# The result was 0.129

print("The result was {r:10.3f}".format(r = result))
# The result was      0.129

##########################################################
# f string literals
##########################################################
name = "Jose"
age = 3

print("Hello, his name is {}".format(name))
# Hello, his name is Jose

print(f"Hello, his name is {name}")
# Hello, his name is Jose

print(f"{name} is {age} years old.")
# Jose is 3 years old.
