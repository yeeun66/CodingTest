# 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 
# 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 
# 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다.
# N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

# 논리를 똑바로 세우면 간단하고 어렵지 않다!!
# 가장 오른쪽 원소를 현재 가장 큰 원소라고 일단 해
# 그리고 이거보다 더 큰 원소를 만나면 그 때 가장 큰 원소를 교채해
# 그래서 이 원소가 또 자기보다 큰 원 소를 만나면 계속 교체해
# 결론은 보이는 막대기, 즉 max값을 계속 찾아서 카운트 해주면 됨!!

import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N) :
    stack.append(int(input()))

cur_max = stack.pop() # pop 함수는 리스트의 원소를 삭제 및 반환
count = 1
while stack :
    temp = stack.pop()
    if temp > cur_max :
        cur_max = temp
        count += 1

print(count)
