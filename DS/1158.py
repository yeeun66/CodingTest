# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성

# 입력 7 3
# 출력 <3, 6, 2, 7, 5, 1, 4>

# index
# 0 1 2 3 4 5 6 
# - - - - - - - <- rear = -1
# 1 2 3 4 5 6 7 <- rear = 2 ; (del 3)
# 1 2 4 5 6 7 <- rear = 4 ; (del 6)
# 1 2 4 5 7 <- rear + (K-1) == 6, 배열 길이 5 ==> rear = rare % 배열 길이, rear = 1 ; (del 2)
# 1 4 5 7 <- rear = 3 (del 7)
# 1 4 5 <- rear + (K-1) == 5, 배열 길이 3 ==> rear = ?, rear = 2 ; (del 5)
# 1 4 <- rear + (K-1) == 4, 배열 길이 2 ==> rear = ?, rear = 0 ; (del 1)
# 4 <- rear + (K-1) == 2, 배열 길이 1 ==> rear = ?, rear = 0 ; (del 4)
# 

# - - - - - - - - 로직 - - - - - - - -
# 원형 큐 원리 약간 사용 # Ex) K = 3, N = 7 일 때
# 아래를 반복. 종료 조건: 리스트 empty
    # rear 초기값 0
    # 조건 2개 => 증가할 값; rear + (K-1) 로 검사
    # rear = rear + (K-1)로 일단 증가
        # 1. 증가한 값이 현재 배열의 길이 보다 작을때
            # 스킵
        # 2. 증가한 값이 현재 배열의 길이와 같거나 클 때 (초과할 때)
            # rear = rare % 배열 길이
    # queue[rear]값 출력
    # del queue[rear]

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = [a+1 for a in range(N)]

print("<", end="")
rear = 0
while queue:
    size = len(queue)
    rear += (K-1)
    if rear >= size : rear = rear % size
    if size == 1 : print(queue[rear], end =">")
    else: print(queue[rear], end =", ")
    del queue[rear]