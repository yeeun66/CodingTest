# 2진수 -> 8진수

# 2진수 배열 엠티까지 아래를 반복
    # 2진수에서 3개 pop해서 
    # 먼저 pop한게 1이면 2^0
    # 두번째로 pop한게 1이면 2^1
    # 세번째로 pop한게 1이면 2^2
    # 이후 3개의 값을 더해서 새로운 배열에 append

    # 배열 3개 미만으로 남았을 때 나머지는 0 취급 하면 됨

# 최종 배열에 저장된 값을 스트링으로 바꾼후 역순로 출력

import sys
input = sys.stdin.readline
num = list(input().strip())

output = []
while num:
    one = 0
    two = 0
    three = 0
    if num : one = num.pop()
    if num : two = num.pop()
    if num : three = num.pop()
    result = 0

    if one == '1' : result += 1
    if two == '1' : result += 2
    if three == '1' : result += 4

    output.append(str(result))

outputs = "".join(output[::-1])
print(outputs)