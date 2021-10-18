import sys
from collections import deque

input = lambda: sys.stdin.readline()

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
  N, L, R = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(N)]  # 각 나라별 인구수
  directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
  n_days = 0

  # 1. 연합인지 확인? bfs? dfs? 국경선 공유하는 나라 인구수 차이 L <= diff <= R : 국경선 오픈
  def check_union(r, c):
    global visited
    union = [(r, c)]  # 연합국 멤버
    visited[r][c] = True
    q = deque()
    q.append((r, c))

    while q:
      c_r, c_c = q.popleft()
      for dr, dc in directions:
        n_r, n_c = c_r + dr, c_c + dc
        if 0 <= n_r < N and 0 <= n_c < N:
          if L <= abs(A[n_r][n_c] - A[c_r][c_c]) <= R and not visited[n_r][n_c]:
            # un list 추가
            union.append((n_r, n_c))
            q.append((n_r, n_c))
            visited[n_r][n_c]=True

    return union

  while 1:
    visited = [[False] * N for _ in range(N)]
    unions = []
    # 서로 다른 연합국이 있을 수도
    for i in range(N):
      for j in range(N):
        if not visited[i][j]:
          un = check_union(i, j)
          if len(un) > 1:
            unions.append(un)

    # 2. 확인 후 인구 나누기
    if unions:  # 연합국 결성 되었으면
      for un in unions:  # unions : 연합국 멤버들 담긴 리스트들
        list_pop = [A[r][c] for r, c in un]
        each_pop = sum(list_pop) // len(list_pop)

        # 인구수 수정
        for r, c in un:
          A[r][c] = each_pop

      # 3. 국경 닫기 중요!!
      n_days += 1
      visited = [[False] * N for _ in range(N)]

    else:  # 연합국 없으면
      break

  print(n_days)