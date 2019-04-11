my_list = [1,2,3]
print(my_list)
print(len(my_list))

your_list = ['one', 'two', 'three']
print(your_list[0])

another_list = ['four', 'five']

print(your_list + another_list)
new_list = your_list + another_list

print(new_list)

# mutate or change elements in a list
new_list[0] = "ONE ALL CAPS"
print(new_list)

# add element to a list
new_list.append('six')
print(new_list)

new_list.append('seven')
print(new_list)

# pop off an item from the end of a list
popped_item = new_list.pop()
print(popped_item)
print(new_list)

popped_item3 = new_list.pop(3)
print(popped_item3)

popped_item_end = new_list.pop(-1)
print(popped_item_end)

alpha_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

print(alpha_list)
alpha_list.sort()
print(alpha_list)

print(num_list)
num_list.sort()
print(num_list)

print(num_list)
num_list.reverse()
print(num_list)
