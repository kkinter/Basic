"""
퀵 정렬
- 정렬 알고리즘의 꽃
- 기준점(pivot 이라고 부름)을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수
- 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복
- 함수는 왼쪽 + 기준점 + 오른쪽을 리턴
"""
def quick_sort(data):
    if len(data) <= 1:
        return data
    left, right = [], []
    pivot = data[0]

    for idx in range(1, len(data)):
        if pivot > data[idx]:
            left.append(data[idx])
        else:
            right.append(data[idx])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def q_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if pivot > item ]
    right = [item for item in data[1:] if pivot <= item ]

    return q_sort(left) + [pivot] + q_sort(right)