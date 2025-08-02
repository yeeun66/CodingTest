# 프린터 큐
'''
큐에 (문서 번호, 중요도) 순으로 추가
큐에서 하나씩 pop하면서, 
    - 뒤에 더 큰 중요도가 있다면, 큐에 다시 매달기
    - 뒤에 더 큰 중요도가 없다면, 
        - 이때 문서 번호가 원하는 번호(M)라면, prt 출력 
        - 아니라면, prt += 1,

'''
from collections import deque
T = int(input())
for _ in range(T) : 
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    que = deque()
    for i in range(len(arr)) : que.append((i, arr[i]))
    cur_list = arr[:] # 현재 남아있는 문서들의 중요도
    prt = 1
    while que : 
        num, score = que.popleft()
        if score >= max(cur_list) : 
            if num ==  M : 
                print(prt)
                break
            prt += 1
            cur_list[num] = 0
        else : 
            que.append((num, score))