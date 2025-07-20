# 로또
# 입력 그냥 한번에 받고 나서 시작 

def backtrack() :
    if len(arr) == 6 : 
        print(*arr)
        return

    for i in range(num) :
        if not arr :
            arr.append(num_list[i])
            backtrack()
            arr.pop()
        elif num_list[i] > arr[-1] :
            arr.append(num_list[i])
            backtrack()
            arr.pop()
            
k = []
n_list = []
idx = 0 # TC 갯수 

while True : # 입력 받기
    tmp_arr = input()
    if len(tmp_arr) == 1 : break
    idx += 1
    tmp_arr = list(map(int, tmp_arr.split()))
    k.append(tmp_arr[0])
    n_list.append(tmp_arr[1:])

for i in range(idx) :
    num = k[i]
    num_list = n_list[i]

    arr = []
    backtrack()
    if i != idx-1 : print()