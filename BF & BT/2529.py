# 부등호 
'''
전체 로직
1. 백트래킹으로 중복 없는 k+1개의 모든 조합 구한 후 -> backtrack, 부호 수열에 만족하는지 검사 -> check_cond
2. check_cond 함수 로직
    - 처음에 2k+1 크기의 빈 배열 생성 후, 부등호는 홀수 배열에 넣어 둔다 
    - 남은 홀수칸에 방금 가져온 숫자를 하나씩 넣어준다 
    - 최종 완성된 배열에서 idx가 홀수일 때, 양 옆의 숫자를 해당 부등호로 비교 수행
        - 한번이라도 틀리면 False 리턴
    - 리턴 안되었다면, True 리턴 
3. check_cond == True 이면, 현재 최대 or 최솟값과 비교해서 업데이트 해주기 (전역 변수)
4. 출력 시 앞에 0 있는 경우 잘 고려해서 K+1 길이로 출력 되도록 최대, 최소 정수 출력
'''

import sys
input = sys.stdin.readline
k = int(input())
inequality = list(map(str, input().split()))
seq = ['' for _ in range(2*k+1)]
j = 0
for i in range(1, 2*k+1, 2) : 
    seq[i] = inequality[j]
    j += 1

max_seq = 0
min_seq = 10000000001

def check_cond(lst) :
    test_seq = seq[:]
    j = 0
    for i in range(0, 2*k+1, 2) :
        test_seq[i] = lst[j]
        j += 1
    
    for i in range(1, 2*k+1, 2) :
        if test_seq[i] == '<' : 
            if int(test_seq[i-1]) > int(test_seq[i+1]) : return False
        if test_seq[i] == '>' :
            if int(test_seq[i-1]) < int(test_seq[i+1]) : return False
    
    return True

exist = set() # 시간초과 방지용 집합
def backtrack() :
    global max_seq
    global min_seq

    if len(arr) == k + 1 :
        tmp = arr[:]
        if check_cond(tmp) : 
            tmp = ''.join(tmp)
            max_seq = max(max_seq, int(tmp))
            min_seq = min(min_seq, int(tmp))
        return
    
    for i in range(10) : 
        if not arr : 
            arr.append(str(i))
            exist.add(i)
            backtrack()
            arr.pop()
            exist.discard(i)
        elif i not in exist : 
            arr.append(str(i))
            exist.add(i)
            backtrack()
            arr.pop()
            exist.discard(i)

arr = []
backtrack()

if len(str(max_seq)) == k+1 : print(max_seq)
else : 
    cnt = k+1 - len(str(max_seq))
    max_tmp = ''
    for _ in range(cnt) : max_tmp += '0'
    print(max_tmp + str(max_seq))

if len(str(min_seq)) == k+1 : print(min_seq)
else : 
    cnt = k+1 - len(str(min_seq))
    min_tmp = ''
    for _ in range(cnt) : min_tmp += '0'
    print(min_tmp + str(min_seq))
