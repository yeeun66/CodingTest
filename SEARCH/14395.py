# 4연산 
# 정수 s의 값을 t로 바꾸는 최소 연산 횟수 구하기 
'''
로직
사용 가능한 연산 (+-*/) /는 0이 아닐 때만 사용 가능

10^9 크기의 배열로 방문 표시
1. 큐에 s 값 넣고 bfs 탐색 시작
    *+-/ 순으로 4가지 탐색 - 연산 후 큐에 넣기
2. 탐색 중 t가 나오면 종료 후 연산 역추적해서 출력하기
    - 부모 자식 관계, dic 에 넣어둔 연산자 활용

'''
import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().split())

if s == t : 
    print(0)
    exit()

def is_inrange(n) : 
    return 0<= n < 1000000001 
parent = {} # 부모 자식 관계
dic = {} # 키 값을 만든 직전 연산자 
visited = set()
visited.add(s)
que = deque([s])
while que :
    x = que.popleft()
    num = -1
    for i in range(4) :
        if i == 0 : 
            num = x * x
            if is_inrange(num) and num not in visited : 
                visited.add(num)
                dic[num] = '*'
                parent[num] = x # num의 부모는 s
                que.append(num)
        elif i == 1 : 
            num = x + x
            if is_inrange(num) and num not in visited : 
                visited.add(num)
                dic[num] = '+'
                parent[num] = x # num의 부모는 s
                que.append(num)
        elif i == 2 : 
            num = x - x
            if is_inrange(num) and num not in visited : 
                visited.add(num)
                dic[num] = '-'
                parent[num] = x # num의 부모는 s
                que.append(num)
        else: 
            if x == 0 : continue
            num = x // x
            if is_inrange(num) and num not in visited : 
                visited.add(num)
                dic[num] = '/'
                parent[num] = x # num의 부모는 s
                que.append(num)
        
        if num == t : break
    if num == t : break

if num != t : 
    print(-1)
    exit()

ouput = []
child = t
while child != s :
    ouput.append(dic[child])
    child = parent[child]

ouput = ouput[::-1]
print(''.join(ouput))
