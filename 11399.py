# ATM (Greedy)
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램
n = int(input())

m = input() # 문자열 한 줄 
a = m.split()

a_int = [] # 정수 리스트
for str in a :
    num = int(str)
    a_int.append(num)

a_int.sort()

sum = 0
for i in range(n) :
    temp = 0
    for k in range(0,i+1) :
        temp += a_int[k]
    sum += temp

print(sum)