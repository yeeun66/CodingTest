# 단어 수학
# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
# 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
# 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
    # 두 수의 합은 99437이 되어서 최대가 될 것이다.
# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하라.

# 문제 접근 포인트 참고: https://edder773.tistory.com/97

# 방법: 
# 1. 각 단어에 있는 알파벳에 대해, 자릿수의 값을 매겨준다
    # Ex) GCF에서 G는 100, C는 10, F는 1
    # 이렇게 매긴 자릿수의 값을 딕셔너리에 저장한다.
    # 이 때 원래 딕셔너리에 있는 값이라면 원래 있던 값에 자릿수의 값을 더해준다
# 2. 딕셔너리의 값들만 내림차순 하여 새로운 리스트에 저장
# 3. num = 9부터 새로 만들어진 리스트에서 하나씩 꺼내면서 num과 곱해서 결과에 더해준다
    # 하나 더하면 num은 1씩 감소

N = int(input())
word = []
for _ in range(N) :
    word.append(list(map(str, input())))

dic = {}
for one in word :
    x = len(one) - 1
    for i in one : 
        if i in dic : dic[i] += 10**x
        else : dic[i] = 10**x
        x -= 1

word_list = sorted(dic.values(), reverse=True) # 값들만 내림차순 정렬

result = 0
num = 9
for i in word_list :
    result += i * num
    num -= 1

print(result)