# File I/O

# Wtires a script that opens a file named 'test.txt', writes 'Hello World' to
# the file, then closes it.

# Forgot parenthese after close
# f = open('test.txt', 'w')
# f.write('Hello World')
# f.close

# These lines of code worked
myfile = open('test.txt','w')
myfile.write('Hello World')
myfile.close()

# Alternate code
# with open('test.txt', mode='w') as f:
#     f.write('Hello World')
