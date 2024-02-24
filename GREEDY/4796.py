# 캠핑
# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작했다. 
# 강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)
# 
# 반례
# 2 4 15
# 0 0 0
# 답: 8, 현재 출력: 9
import sys
input = sys.stdin.readline

i = 0
s = []
while True :
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0 :
        break
    day = 0
    a = V // P
    day += a*L
    if V - a*P < L :
        day += (V -a*P) 
    else : day += L
    s1 = 'Case {0}: {1}'.format(i+1, day)
    s.append(s1)
    i += 1
for k in range(i) :
    print(s[k])