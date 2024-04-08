"""
스택
- 데이터를 제한적으로 접근할 수 있는 구조
  > 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
- 가장 나중에 쌓은 데이터를 가장 먼저 뺄 수 있는 구조
  > 큐 : FIFO
  > 스택 : LIFO 
장단점
- 장점
  > 구조가 단순해서, 구현이 쉽다.
  > 데이터 저장/읽기 속도가 빠르다.
- 단점
  > 데이터 최대 갯수를 미리 정해야 한다.
  > 저장 공간의 낭비가 발생할 수 있음.
"""
def reculsive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        reculsive(data - 1)
        print("returned", data)
reculsive(4)

data_stk = []

data_stk.append(1)
data_stk.append(2)

data_stk.pop()
print(data_stk)
stk = []
def push(data):
    stk.append(data)
def pop(data):
    data = stk[-1]
    del stk[-1]
    return data