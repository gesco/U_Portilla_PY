# mode='r' is read only
# mode='w' is write only (will overwrite files or create new!)
# mode='a' is append only (will add on to files)
# mode='r' is reading and writing
# mode='w+' is writing and reading (Overwrites existing files or creates a
# new file!)

# with open('my_new_file.txt', mode='r') as f:
#     print(f.read())
# ONE ON FIRST
# TWO ON SECOND
# THREE ON THIRD

with open('my_new_file.txt', mode='a') as f:
    print(f.write("\nFOUR ON FOURTH"))

with open('my_new_file.txt', mode='r') as f:
    print(f.read())

with open('aidp.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')
