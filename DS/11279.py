# 최대 힙
import sys; input = sys.stdin.readline
import heapq
arr = []
N = int(input())

for _ in range(N) : 
    x = int(input())
    if x == 0 : 
        if not arr : sys.stdout.write('0' + "\n")
        else : 
            result = heapq.heappop(arr)* -1
            sys.stdout.write(str(result) + "\n")
    else : 
        heapq.heappush(arr, -x)
