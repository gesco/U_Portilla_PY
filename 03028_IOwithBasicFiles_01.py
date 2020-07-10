myfile = open('myfile.txt')

print(myfile.read())
myfile.seek(0)
print(myfile.read())
# Hello this is a text file
# this is the second line
# this is the third line
#
# Hello this is a text file
# this is the second line
# this is the third line

myfile.seek(0)
contents = myfile.read()
print(contents)
# Hello this is a text file
# this is the second line
# this is the third line

myfile.seek(0)
print(myfile.readlines())
# ['Hello this is a text file\n', 'this is the second line\n', 'this is the third line\n']

myfile.close()

###########################################
# with open('myfile.txt') as my_new_file: #
#     contents = my_new_file()            #
###########################################
