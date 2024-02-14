# 이 아파트에 거주를 하려면 
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력
# 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())

for _ in range(T) :
    k = int(input())
    n = int(input())
    a = [i for i in range(1, n+1)] # 0층 리스트
    for _ in range(k) :
        for i in range(1, n) :
            a[i] += a[i-1]
    print(a[-1])