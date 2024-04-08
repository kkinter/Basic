"""
큐
- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
  > 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것
  > FIFO 또는 LILO
용어
- Enqueue :
- Dequeue :
어디에 큐가 많이 쓰일까?
- 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨()
"""

import queue

data_queue = queue.Queue()

data_queue.put('1')
data_queue.put('2')
data_queue.get()
print(data_queue.qsize())

# Lifo 큐 만들기
lifo_queue = queue.LifoQueue()

que = []
prior_queue = queue.PriorityQueue()
prior_queue.put((10, "korea"))
prior_queue.put((5, "1"))
prior_queue.put((15, "3"))

print(prior_queue.get())
d_q = []
def enqueue(data):
  d_q.append(data)

def dequeue():
  data = d_q[0]
  del d_q[0]
  return data

  
from collections import deque


