# 이모티콘

'''
* 3가지 연산 (각 연산당 1초 걸림)
a. 모두 복사 
b. 모두 붙여 넣기
c. 하나 지우기

처음에 1개 존재. S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값 구하기
S == 2 : a, b -> 2초
S ==  4 : a, b, a, b -> 4초
S == 6 : a, b, a, b, b -> 5초
S == 18 : a, b, a, b, b, a, b, b -> 8초

로직
숨바꼭질이랑 비슷한 듯 
1. que에 처음에 (1, -1, 0) 넣고 bfs 시작
2. 큐에서 하나씩 pop하며 세가지 연산 수행 
    val, ste, depth = que.popleft()
    ste == -1 이면, 복사랑 지우기만 가능 
    1) 복사하기. val != 0 일 때, (현재값, 복사한 값, depth+1)를 큐에 저장
    2) 붙여넣기. ste != -1 일때, (val+ste, ste, depth+1)를 큐에 저장
    3) 1 감소. val > 2 일 때, (val-1, ste, depth+1)를 큐에 저장 
3. val이 S이면 현재 depth 출력, 즉시 종료

- 시간초과 날까봐 visit 집합 이용해서 (val, ste) 같은건 큐에 넣지 않도록 함

'''
import sys
from collections import deque
input = sys.stdin.readline
S = int(input())

que = deque()
que.append((1, -1, 0))
visit = set()
visit.add((1, -1))
while que : 
    val, ste, depth = que.popleft()
    
    if depth > 25 : continue
    if val == S : 
        print(depth)
        exit()
    for i in range(3) :
        if i == 0 : 
            if val != 0 : 
                if (val, val) in visit : continue
                que.append((val, val, depth+1))
                visit.add((val, val))
        elif i == 1 :
            if ste != -1 : 
                if (val+ste, ste) in visit : continue
                que.append((val+ste, ste, depth+1))
                visit.add((val+ste, ste))
        else : 
            if val > 2 : 
                if (val-1, ste) in visit : continue
                que.append((val-1, ste, depth+1))
                visit.add((val-1, ste))
