def findSmallest(arr):
	smallest = arr[0]      # 가장 작은 정수를 저장합니다.
	smallest_index = 0     # 가장 작은 정수의 인덱스를 저장합니다.

	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i

	return smallest_index


def selectionSort(arr):    # 배열을 정렬합니다.
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)        # 배열에서 가장 작은 정수를 찾아서 새로운 배열에 추가합니다.
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))
