# queue and graph

from collections import deque


def person_is_seller(name):
	return name[-1] == 'm'

def search(name):
	search_queue = deque()    # 새 큐를 생성
	search_queue += graph[name]    # 모든 이웃을 탐색 큐에 추가
	searched = []    # 이 배열은 이미 확인한 사람을 추적하기 위한 것

	while search_queue:    # 큐가 비어 있지 않는 한 계속 실행
		person = search_queue.popleft()
		if person_is_seller(person):    # 망고 판매상인지 확인
			print(person + "is a mango seller!")    # 망고 판매상이 맞음
			return True
		else:
			search_queue += graph[person]    # 망고 판매상이 아님. 모든 이웃을 탐색 목록에 추가
	return False
