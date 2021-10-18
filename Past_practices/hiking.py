import sys
input = sys.stdin.readline

def digging(dir, k, cum):
    global ans
    visited[dir[0]][dir[1]] = True

    if cum > ans:
        ans = cum

    for d in direction:
        nx, ny = d[0]+dir[0], d[1]+dir[1]

        if nx<0 or nx>=n or ny<0 or ny>=n or visited[nx][ny]: # 이미 방문, 맵 밖 처리
            continue

        if road[nx][ny] < road[dir[0]][dir[1]]: # 다음 것이 더 작아
            digging((nx,ny), k, cum+1)

        elif road[nx][ny] - k < road[dir[0]][dir[1]] and k:  # 깎을 수 있을 때
            tmp = road[nx][ny]
            road[nx][ny] = road[dir[0]][dir[1]] - 1
            digging((nx,ny), 0, cum+1)
            road[nx][ny] = tmp

    visited[dir[0]][dir[1]] = False

T = int(input())
for t in range(T):

    n, k = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(n)]

    max_h = 0
    max_q = []

    # 가장 높은 봉우리 시작
    for i in range(n):
        for j in range(n):
            if road[i][j]>max_h:
                max_h = road[i][j]
                max_q.clear()
                max_q.append((i,j))
            elif road[i][j]==max_h:
                max_q.append((i,j))

    # 높은 -> 낮은 : 가로 or 세로 (대각선 x)
    direction = ((-1,0),(0,1),(1,0),(0,-1))
    ans = 0

    for q in max_q:
        #print(q)
        visited = [[False]*n for _ in range(n)]
        digging(q,k,1)

    print("#{}".format(t+1), ans)

