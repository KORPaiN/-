n = int(input())
move = list(map(str, input().split()))
x, y = 1, 1 #행, 열
dx = [0,0,-1,1] #행이동 LRUD
dy = [-1,1,0,0] #열이동 LRUD
move_types = ['L','R','U','D']

for p in move:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
#왼쪽 위-첫 시작 (1,1), 오른쪽 아래(N,N)

#L : y-1
#R : y+1
#U : x-1
#D : x+1

#공간을 벗어나는 행동은 무시
