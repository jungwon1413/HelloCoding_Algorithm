def quicksort(array):
	if len(array) < 2:
		return array    # 기본 단계: 원소의 개수가 0이나 1이면 이미 정렬되어 있는 상태

	else:
		pivot = array[0]    # 재귀 단계
		less = [i for i in array[1:] if i <= pivot]    # 기준 원소보다 작거나 같은 모든 원소로 이루어진 하위 배열
		greater = [i for i in array[1:] if i > pivot]  # 기준 원소보다 큰 원소로 이루어진 하위 배열
		return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
