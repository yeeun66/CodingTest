# 에너지 모으기
'''
로직

1. 백트래킹 상태 관리 - backtrack(현재 배열, 현재 배열 길이, 현재 에너지)
- 제거할 x(인덱스로) 선택 후 백트래킹 - 이때 처음과 마지막은 선택될 수 없음
2. 백트래킹 종료 조건 
    - 현재 배열 길이가 2일 때 
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_energy = 0

def backtrack(lst, l, nxt_energy) : 
    global max_energy

    if l == 2 : 
        max_energy = max(max_energy, nxt_energy)
        return
    
    for i in range(1, l-1) : 
        nxt_lst = lst[:i] + lst[i+1:]
        nxt_energy += lst[i-1] * lst[i+1]
        backtrack(nxt_lst, l-1, nxt_energy)
        nxt_energy -= lst[i-1] * lst[i+1]

backtrack(arr, N, 0)
print(max_energy)