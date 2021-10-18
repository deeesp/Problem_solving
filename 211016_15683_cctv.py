import sys
from copy import deepcopy
sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline()

T = int(input())
for test_case in range(1, T + 1):
  N, M = map(int, input().split())  # 1x1 ~ 8x8
  office = [list(map(int, input().split())) for _ in range(N)]  # 0 : 빈칸, 6: 벽, 1~5 : CCTV 종류
  cctvs = [(v, i, j) for i, row in enumerate(office) for j, v in enumerate(row) if 0 < v < 6]
  cctvs.sort(reverse=True)  # 5번 먼저
  n_cctv = len(cctvs)
  min_blind = 99999

  # 회전시킬 수 있음
  cctv = {1: [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],  # 4회전
          2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],  # 2회전
          3: [((0, 1), (-1, 0)), ((-1, 0), (0, -1)), ((0, -1), (1, 0)), ((1, 0), (0, 1))],  # 4회전
          4: [((0, 1), (-1, 0), (0, -1)), ((-1, 0), (0, -1), (1, 0)), ((0, -1), (1, 0), (0, 1)),
              ((-1, 0), (0, 1), (1, 0))],  # 4회전
          5: [((0, 1), (-1, 0), (0, -1), (1, 0))]}  # 회전 x

  def dfs(maps, depth):
    global min_blind

    if depth == n_cctv:  # CCTV 대수 만큼 다 찼을 때 계산
      num_blind = sum([row.count(0) for row in maps])
      min_blind = min(min_blind, num_blind)
      return

    n, r, c = cctvs[depth]
    for dirs in cctv[n]:  # 회전 경우의 수
      monitor = beam(deepcopy(maps), dirs, r, c)
      dfs(monitor, depth + 1)

  # 해당 방향 감시 체크
  def beam(maps, dirs, r, c):
    for di, dj in dirs:
      x = 1
      while 1:
        n_r = r + (x * di)
        n_c = c + (x * dj)
        if 0 <= n_r < N and 0 <= n_c < M and maps[n_r][n_c] != 6:
          maps[n_r][n_c] = 7
          x += 1
        else:
          break
    return maps

  dfs(deepcopy(office), 0)

  # 사각 지대의 최소 크기
  print(min_blind)