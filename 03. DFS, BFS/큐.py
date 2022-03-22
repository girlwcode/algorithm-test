# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조 활용
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)

# 역순으로 바꾸기 (나중에 들어온 원소부터 출력)
queue.reverse()
print(queue)

# deque를 리스트형으로 형변환
queue_list = list(queue)
print(queue)