N = int(input())
cafe = [list(map(int, input().split())) for _ in range(N)]
dir = ((1,1), (1,-1), (-1,-1), (-1,1))
max_d = -1

# 중복 있으면 안됨
# 무조건 대각선
# 같은길 돌아가는 것 안됨
# 경우의 수


def go(i, j, k, n):
    global si, sj, max_d

    print(i,j,k,n)

    if k==3 and i==si and j == sj: # 출발점에 도착한 경우
        if max_d < n:
            max_d = n
            print(max_d)

    if i<0 or i>=N or j<0 or j>=N : # 맵 밖
        return

    elif cafe[i][j] in q: # 같은 디저트가 있는 경우
        return

    else:
        q.append(cafe[i][j])

        if k==0 or k==1:
            go(i+dir[k][0], j+dir[k][1], k, n+1)
            go(i+dir[k+1][0], j+dir[k+1][1], k+1, n+1)
        elif k==2:
            if i+j != si+sj:
                go(i + dir[k][0], j + dir[k][1], k, n + 1)
            else:
                go(i + dir[k + 1][0], j + dir[k + 1][1], k+1, n + 1)
        else:
            go(i + dir[k][0], j + dir[k][1], k, n + 1)

        q.remove(cafe[i][j])


q = []
for i in range(N):
    for j in range(1,N-1):
        si = i
        sj = j
        q.append(cafe[i][j])
        go(i+1, j+1, 0, 1)
        q.remove(cafe[i][j])

print(max_d)