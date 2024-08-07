# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성
# 첫 줄: 출입 기록의 수 n
# 다음 n개의 줄에는 출입 기록이 순서대로 주어짐. 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어짐
# 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

# 딕셔너리 써서 어차피 마지막에 나갔으면 leave로 뜰거니까 입력 다 받은 후에, enter인 사람만 카운트하기

import sys
input = sys.stdin.readline

N = int(input()) 
d = {} # 딕셔너리 선언
for _ in range(N) :
    name, state = map(str, input().split())
    d[name] = state

result = []
for k in d.keys() :  # 딕셔너리의 key 리스트
    if d[k] == 'enter' :
        result.append(k)

result.sort(reverse=True) # 사전 역순
print("\n".join(result)) # 줄간격 하나 줘서 리스트 하나씩 출력