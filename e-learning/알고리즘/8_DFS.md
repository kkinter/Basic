## DFS

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-20-11-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-20-50-image.png)

### 방문 기준은 문제에서 요구하는 내용에 따라 달라질 수 있음

흔히 DFS 를 설명할 땐, 방문 기준이 번호가 낮은 인접 노드 부텅미

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-22-06-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-22-12-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-22-49-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-23-07-image.png)

DFS는 깊이 우선 >> 그래프에서 가장 깊은 곳을 탐색

더이상 들어갈 수 없다면 다른 방향으로 

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-23-35-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-23-45-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-23-52-image.png)

2차원 구조 ? 인접한 노드가 무엇인지 리스트 형태로 담아둘 수 있음

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-24-26-image.png)

인덱스 0을 사용하지 않기 위해 하나 더 큰 9를 곱해줌

그래프에 대한 정보, 방문 정보가 기록되어 있는 리스트를 활용

재귀적으로 방문하지 않은 요소들을 

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-28-04-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-07-25-02-28-46-image.png)
