# 최소 힙
# 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys
import heapq as hq

input = sys.stdin.readline
N = int(input()) # 연산의 갯수]
queue = []
for _ in range(N) :
    x = int(input())
    if x == 0 : 
        if len(queue) == 0 : print(0)
        else : 
            a = hq.heappop(queue)
            print(a)
    else :
        hq.heappush(queue, x)