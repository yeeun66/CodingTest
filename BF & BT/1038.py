# 감소하는 수 
# 이거 백트래킹 아님 -> 그냥 큐로 품 
'''
0~9 -> 그대로 모두
10~19 -> 10
20~29 -> 20, 21
30~39 -> 30, 31, 32
40~49 -> 40, 41, 42, 43
...
90~99 -> 90, 91, ... , 98
100~999 -> 210, 310, 321, 320, 410, 420, 421, 432, 431, 430, ... 
'''

'''
로직
N번째 감소하는 수 만날 때 까지 다음을 반복 
1. 우선 순위 큐에 0~9 넣어두기
2. 우선 순위 큐에서 하나씩 pop 하면서 increase 실행
    - 현재 pop한 x가 N이면 출력하고 프로그램 종료 
3. increase 실행 후 자신의 뒤에 감소하는 수를 붙여서 힙큐에 추가 
'''

import heapq
N = int(input())

cnt = -1
que = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def increase() : # 이건 백트래킹 로직이 아니긴 해 
    global cnt

    cnt += 1
    if cnt == N : 
        print(x)
        exit()
    return 
    
while True :
    if N > 1022 : break
    x = heapq.heappop(que)
    increase()

    tmp = list(str(x))
    last = int(tmp[-1])
    prev = x
    for i in range(10) :
        if i < last : 
            x = x*10 + i 
            heapq.heappush(que, x) 
            x = x // 10
            
print(-1)