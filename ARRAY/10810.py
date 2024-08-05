# 바구니를 총 N개 (1~N번)
# (+) 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다

# 앞으로 M번 공을 넣으려고 한다 (공 넣는 횟수)
# 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다
# 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다
# M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성

# 예제 
# N, M
# i j k [i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다]
# i j k
#  ... (M 만큼)
# i j k 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [0] * N

for _ in range(M) : 
    i, j, k = map(int, input().split())
    n  = j-i+1
    for _ in range(n) :
        a[i-1] = k
        i += 1

print(*a)