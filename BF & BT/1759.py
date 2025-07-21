# 암호 만들기 
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성
'''
서로 다른 L개의 알파벳으로 구성, 최소 한개의 모음, 최소 2개의 자음, 오름차순

1. n_list를 오름차순으로 정렬
2. 중복없이 L개의 수열을 구하는 백트래킹 수행
    - 배열 길이가 L개가 되면, 모음-자음 유효성 체크 (함수로 따로 구현)
    - 가능한 암호라 판단되면 출력 후 리턴 

'''

L, C = map(int, input().split())
n_list = list(map(str, input().split()))

n_list = sorted(n_list)

def check(lst) :
    mo, ja = 0, 0
    for ls in lst : 
        if ls in ('a', 'e', 'i', 'o', 'u') : mo += 1
        else : ja += 1
    
    if mo >= 1 and ja >= 2 : return True
    else : return False

def backtrack() :
    if len(arr) == L :
        if(check(arr)) : print(''.join(arr))
        return
    
    for i in range(len(n_list)) :
        if not arr : 
            arr.append(n_list[i])
            backtrack()
            arr.pop()  
        elif n_list[i] > arr[-1] : 
            arr.append(n_list[i])
            backtrack()
            arr.pop()        

arr = []
backtrack()