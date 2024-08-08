# 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램
# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력

# 딕셔너리로 key: 종 이름, value: 등장 횟수 세면 좋을 것 같은데

import sys
input = sys.stdin.readline

s = set() # 집합
d = {} # 딕셔너리
while True :
    string = input().strip()
    if string == "" : break
    
    if string in s :
        d[string] += 1
    else:
        d[string] = 1
        s.add(string)

sorted(d.items())
total = len(s)
print(total)
for i in d :
    result = d[i] / total * 100
    d[i] = result
    # print("i: ", i, " d[i]: ", d[i])
    print(f'{i} {d[i]:.4f}')

print(d)


