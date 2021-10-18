import sys
import copy
from collections import deque
from itertools import combinations

#sys.stdin = open("input_lab.txt", "r")
input = lambda: sys.stdin.readline()

#T = int(input())
#for test_case in range(1, T + 1):
# 벽(1)을 놓아 바이러스(2) 차단 : 벽 3개 놓을 수 있음
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
max_safe = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)  # 바이러스 상하좌우 인접한 빈칸 퍼짐
virus_idx = [(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == 2]

# 1. 벽 3개 조합
wall_candidate = [(i, j) for i, row in enumerate(grid) for j, value in enumerate(row) if value == 0]
wall_comb = list(combinations(wall_candidate, 3))

# 2. 각 조합별 벽 3개 설치 후 안전 영역 count
for walls in wall_comb:
  num_safe = 0
  tmp = copy.deepcopy(grid)
  for x, y in walls:
    tmp[x][y] = 1

  def bfs():
    q = deque(virus_idx)
    while q:
      i, j = q.popleft()
      for di, dj in zip(dx, dy):  # 상하좌우 바이러스 전파
        i_next = i + di
        j_next = j + dj
        if 0 <= i_next < N and 0 <= j_next < M:  # 맵 내부 존재
          if tmp[i_next][j_next] == 0:
            tmp[i_next][j_next] = 2
            q.append((i_next, j_next))
  bfs()

  # def dfs(i, j):  # 상하좌우 바이러스 전파
  #   if tmp[i][j] == 2:  # virus면 전파
  #     for di, dj in zip(dx, dy):
  #       i_next = i + di
  #       j_next = j + dj
  #       if i_next >= 0 and i_next < N and j_next >= 0 and j_next < M: # 맵 내부 존재
  #         if tmp[i_next][j_next]==0: # 0이면 전파
  #           tmp[i_next][j_next]=2
  #           dfs(i_next, j_next)
  #
  # # 모든 바이러스 숙주에 대해 전파
  # for v_i, v_j in virus_idx:
  #   dfs(v_i, v_j)

  # 안전 영역 최대크기 구하기
  num_safe = sum([row.count(0) for row in tmp])
  max_safe = max(num_safe, max_safe)

print(max_safe)
