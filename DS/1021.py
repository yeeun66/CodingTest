# 회전하는 큐
# N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
# 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
    # 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
    # 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
    # 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 
# 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N, M = map(int, input().split()) # 큐의 크기, 뽑아낼 개수

for i in range(N) : 
    queue.append(i+1)

m = list(map(int, input().split()))

count = 0
for i in range(M) :
    fir = queue[0]
    while queue :
            
        if m[i] == queue[0] : 
            queue.popleft()
            break

        if queue.index(m[i]) >= len(queue) / 2 :
            queue.rotate(1) # 오른쪽으로 회전
        else : queue.rotate(-1) # 왼쪽으로 회전 
        count += 1
    
print(count)