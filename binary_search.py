# -*- coding: utf-8 -*-

def binary_search(list, item):    # This code will not work properly in python3, since 'mid' becones float number.
	low = 0.0
	high = len(list) - 1

	while low <= high:
		mid = (low + high) / 2
		print(mid)
		guess = list[int(mid)]

		if guess == item:
			return mid

		if guess > item:
			high = mid - 1

		else:
			low = mid - 1

	return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))    # => 1
print(binary_search(my_list, -1))   # => None
