# AC
# AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
    # 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, 
    # D는 첫 번째 수를 버리는 함수이다. 
    # 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
# 함수는 조합해서 한 번에 사용할 수 있다. 
    # 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
    # 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성
    #만약, 에러가 발생한 경우에는 error를 출력한다.

# 4 ==> TC 수 
# RDD ==> 수행할 함수 
# 4 ==> 배열 길이
# [1,2,3,4] ==> 배열 값
# ... TC 만큼 반복

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    func = list(map(str, input().strip()))
    ar_num = int(input())
    string = input().strip() # [1,2,3,43]
    arr = deque()
    num = '' 
    for i in string :
        if i.isdigit() : # 정수이면 넣을건데
            num += i # 여러자리 일수도 있으니까 콤마 만날때까지 더해줘
        if i == ',' or i == ']':
            arr.append(num)
            num = '' # 다시 다음 숫자 담으려면 초기화

    if '' in arr : arr.pop() # 아무것도 없으면 기본적으로 '' 담기기 때문에 예외처리
    
    err_flag = 0
    r = 0
    for i in func :
        if i == 'R' : r += 1
        if i == 'D' : 
            if arr :
                if r % 2 == 0 : arr.popleft()
                elif r % 2 == 1 : arr.pop()
            else : err_flag = 1

    a = list(arr) # 큐를 리스트로 변환 (출력 때문에)     
    int_list = [int(x) for x in a] # 문자열 정수로 변환

    if err_flag == 1 : print("error")
    elif not int_list: print(int_list)
    else : 
        if r % 2 == 1 : int_list = int_list[::-1]
        result = '[' + str(int_list[0])
        cnt = 0
        for i in int_list :
            if cnt == 0 : 
                cnt += 1
                continue
            result += ','
            result += str(i)
        result += ']'
        print(result)