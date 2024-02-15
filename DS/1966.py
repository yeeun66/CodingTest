# 아직 하는 중 

# 프린터 큐
# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 
# 그렇지 않다면 바로 인쇄를 한다.
# 할 일은 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

from collections import deque

N = int(input())

for _ in range(N) :
    key = deque()
    n_m = list(map(int, input().split()))
    keys = list(map(int, input().split()))
    dic = {}
    for i in range(n_m[0]) :
        key.append(keys[i])
        dic[i] = keys[i]
    print(dic)
    i = 0
    # want = key[n_m[1]] # 이렇게 하면 같은 숫자 있을 때 구분 못해 -> 무조건 인덱스로 가야할 듯
    want = dic.get(n_m[1])
    print("want: ", want)
    while True :
        max_v = max(key)
        p = key.popleft()
        if max_v > p :
            key.append(p)
        else : 
            goal = i
            i += 1
            if p == want : 
                print(i)
                break