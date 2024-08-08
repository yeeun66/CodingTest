# 절댓값 힙
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
# 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 첫째 줄에 연산의 개수 N (N>=1)이 주어진다. 
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
# x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 

# 아니 나는 이걸 왜 못풀어?
import sys
import heapq as hq
input = sys.stdin.readline
queue = []

N = int(input())
for _ in range(N) :
    x = int(input())
    if x < 0 : x = -x
    if x == 0 and queue :
        # a = hq.heappop(queue)
        # hq.heappop(queue, a)
        print("ans: ", hq.heappop(queue))   
    else :
        hq.heappush(queue, x)

         