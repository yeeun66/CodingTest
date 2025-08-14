# 숫자 카드 2
# 이분 탐색 연습용 문제
'''
로직 (시간초과)
cards는 set에 넣어서는 안됨
대신 targets은 set에 넣어도 됨
타겟 t에 대한 갯수는 dic[t]에 저장
1. targets에서 하나씩 꺼내며 cards에 몇개 있는지 탐색
    - 이분탐색 구현: 하나 찾으면 그 값은 inf로 바꾸고 다시 탐색, 없을 때 까지 탐색
2. 탐색한 갯수 dic[t]에 저장
3. targets에서 하나씩 꺼내며, dic[t]에 있는 것 출력
'''
'''
! 시간초과 해결 로직 - 처음 로직에서 1번 (이분 탐색 구현) 수정
1. targets에서 하나씩 꺼내며 cards에 몇개 있는지 탐색
    - 이분탐색 구현: 하나 찾으면, 거기서 양 옆으로 다시 탐색
        - 타겟 보다 작거나 큰 값이면 종료
'''
import sys; input = sys.stdin.readline
INF = 10000001
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

def binary_search(target, start, end) : 
    cnt = 0

    while start <= end : 
        mid = (start + end) // 2
        if cards[mid] == target : 
            cnt += 1
            left, right = mid-1, mid+1
            if left >= 0 : 
                while cards[left] == target : 
                    cnt += 1
                    left -= 1
                    if left < 0 : break
            if right <= N-1 : 
                while cards[right] == target : 
                    cnt += 1
                    right += 1
                    if right > N-1 : break
            
            return cnt

        elif cards[mid] > target : 
            end = mid -1
        else : 
            start = mid +1

    return cnt 

cards.sort()
target_set = set(targets)
dic = {}
for t in target_set : 
    result = binary_search(t, 0, N-1) 
    dic[t] = result 

for t in targets : sys.stdout.write(str(dic[t]) + " ")