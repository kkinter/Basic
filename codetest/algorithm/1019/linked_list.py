"""
링크드 리스트
- 구조
  > 연결 리스트라고 함
  > 배열은 순차적으로 연결된 공간에 데이터를 나영하는 데이터 구조
  > 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
  > 본래 C언어에서는 주요한 데이터 구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
- 구조와 용어

- 장단점
  > 미리 데이터 공간을 할당하지 않아도 됨.
     배열은 미리 데이터 공간을 할당 해야 함
  단점
     - 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
     - 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
     - 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야하는 작업 필요

"""

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 
# 객체는 2번 만들고, 연결은 안됨
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1
       
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    #헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
	
    #모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node


    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next