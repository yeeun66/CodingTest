# 최솟값 찾기

# N개의 수 A1, A2, ..., AN과 L이 주어진다.
# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성
# i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

# 논리1) 배열 슬라이싱을 L 만큼 해서 그 때마다 구한 최솟값을 프린트
#   최소값 구할 때는 반복문 보다 최소힙을 사용하면 더 빠를 것으로 예상 
# --> 반복문 3개 사용으로 시간초과.

# 논리2) 윈도우 슬라이싱 기법. deque 사용  
#   큐에 (index, value) 를 넣어야 함
# 윈도우, 즉 큐에 넣고 있을 값 범위를 L로 정한후  어떤 조건에 따라 꺼내거나 넣는 방식으로 큐를 관리한다.
    # 조건1) 현재 인덱스 - 가장 왼쪽 인덱스 >= L 인경우 )) 이제 가장 왼쪽은 필요없으니까 popleft()한다.
    # 조건2) 큐에 들어갈 수 있는 경우 )) 현재 남아 있는 최소값 vs 들어오려는 value. 들어오려는 값이 더 작을 경우에 큐에 삽입. 
            # 이때 dq의 끝값이 들어오려는 값보다 크면 pop(). 
            # pop()할 때는 큐가 비어있는지도 확인해야함
# 그래서 반복문 마다 최솟값을 출력)) dq[0][1]

# 추가는 일단 하는데
    # 1. 먼저, 추가 할 값과 현재 맨뒤의 값 중 추가할 값이 더 작으면, 현재 맨 뒤 값을 제거   
    # 2. 그러고 이제 추가    
    # 3. 추가한 인덱스와 맨앞의 인덱스 비교해서 맨앞을 제거할지 결정
    # 4. 프린트

import sys
from collections import deque

input = sys.stdin.readline
N, L = map(int, input().split())
a = list(map(int, input().split(' ')))
dq = deque()

dq.append((0, a[0]))
print(dq[0][1], end=' ')

for i in range(1, N) :
    while dq and a[i] < dq[-1][1] :
        dq.pop()
    
    dq.append((i, a[i]))

    if i - dq[0][0] >= L : dq.popleft()
    
    print(dq[0][1], end=' ')