import sys, heapq
input = lambda: sys.stdin.readline()

# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for test_case in range(1, T + 1):
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]  # 0: 빈칸, 1,2,3,4,5,6: 물고기 크기, 9: 아기상어 위치
direction = ((-1, 0), (0, -1), (1, 0), (0, 1))
q = [(0, i, j) for i in range(N) for j in range(N) if grid[i][j] == 9]

heapq.heapify(q)
_, i, j = q[0]
grid[i][j] = 0

body, eat, time = 2, 0, 0
visited = [[False] * N for _ in range(N)]  # 왔는지 체크할 것이 필요

while q:
  d, x, y = heapq.heappop(q)
  visited[x][y] = True

  if 0 < grid[x][y] < body:  # 자기보다 작은 물고기 먹기
    eat += 1
    grid[x][y] = 0

    if eat == body:  # 몸 커지기
      body += 1
      eat = 0

    time += d
    d = 0

    q.clear()
    visited = [[False] * N for _ in range(N)]

  for dx, dy in direction:
    nd, nx, ny = d + 1, x + dx, y + dy
    # 좌표 범위 내 & 방문 한적 없음 & 크기 작거나 같을 때 이동
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and 0 <= grid[nx][ny] <= body:
      visited[nx][ny] = True
      heapq.heappush(q, (nd, nx, ny))

print(time)
