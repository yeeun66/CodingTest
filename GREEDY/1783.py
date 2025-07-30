# 병든 나이트
# 병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력

'''
로직 (greedy)
N과 M에 따라 경우의 수 잘 따져서 계산
N == 1 : M과 상관 없이 무조건 1
N == 2 : 
    - M > 6 일때는 계속 4
    - M <= 6일 때는 (M+1)//2
    => 정리하면 min(4, (M+1)//2)
N >= 3 : 
    - 5 <= M <= 6일 때는 최대 4
    - M < 5 일때는 M
    => 정리하면 M <= 6일 때, min(4, M)
N >= 3 : 
    - M > 6 일때는 M-2 
'''

import sys; input = sys.stdin.readline

N, M = map(int, input().split())

if N == 1 : print(1)
elif N == 2 : print(min(4, (M+1)//2))
elif M <= 6 : print(min(4, M))
else : print(M-2)