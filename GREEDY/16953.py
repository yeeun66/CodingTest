# A -> B
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음 두 가지
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값 구하기 

# BFS로도 풀이 가능 (나중에 해보기)

# m이 1로 끝날 때에는 10으로 나누고 2로 나누어 떨어질 땐 2로 나누는 식의 풀이
# top-down으로 생각 (b를 a로 만들자)

a, b = map(int, input().split())
count=0
while a!=b:
    if a>b:
        count=-2
        break
    elif str(b)[-1]=='1': # 끝이 1 이면 10으로 나눈 몫을 b에 넣기 
        b=b//10
        count+=1
    elif b%2==0: # 짝수면 2로 나누기 
        b=b//2
        count+=1
    else:
        count=-2
        break
print(count+1)