my_list = [1,2,3]
print(my_list)
# [1, 2, 3]
print(len(my_list))
# 3

your_list = ['one', 'two', 'three']
print(your_list[0])
# one

another_list = ['four', 'five']

print(your_list + another_list)
# ['one', 'two', 'three', 'four', 'five']

new_list = your_list + another_list
print(new_list)
# ['one', 'two', 'three', 'four', 'five']

# mutate or change elements in a list
new_list[0] = "ONE ALL CAPS"
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five']

# add element to a list
new_list.append('six')
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

new_list.append('seven')
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']

# pop off an item from the end of a list
popped_item = new_list.pop()
print(popped_item)
# seven
print(new_list)
# ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']

popped_item3 = new_list.pop(3)
print(popped_item3)
# four

popped_item_end = new_list.pop(-1)
print(popped_item_end)
# six

alpha_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]

print(alpha_list)
# ['a', 'e', 'x', 'b', 'c']
alpha_list.sort()
print(alpha_list)
# ['a', 'b', 'c', 'e', 'x']

print(num_list)
# [4, 1, 8, 3]
num_list.sort()
print(num_list)
# [1, 3, 4, 8]

print(num_list)
# [1, 3, 4, 8]
num_list.reverse()
print(num_list)
# [8, 4, 3, 1]
