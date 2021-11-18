
# [기초=리스트] 바둑알 십자 뒤집기
h,w = input().split()
arr = [[0 for col in range(int(w))] for row in range(int(h))]

n = int(input())
for i in range(n):
    l,d,x,y = input().split()
    l = int(l) # 막대 길이 
    d = int(d) # 가로/세로 
    x = int(x)-1 # 행 
    y = int(y)-1 # 열 

    for j in range(l):
        if d ==0:
           arr[x][y+j] = 1
        else:
            arr[x+j][y] = 1

for i in range(int(h)):
    for j in range(int(w)):
        print(arr[i][j], end=" ")
    print()
