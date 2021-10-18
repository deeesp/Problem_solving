import sys
from copy import deepcopy

input = lambda: sys.stdin.readline()
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
  R, C, T = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(R)]

  directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
  dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
  zero_map = [[0] * C for _ in range(R)]

  cleaner_up, cleaner_down = 0, 0  # 공기청정기 좌표 [cleaner_up][0], [cleaner_up+1][0]
  for a in range(len(A)):
    if A[a][0] == -1:
      cleaner_up, cleaner_down = a, a+1
      break


  def spread():
    global A
    draw = deepcopy(zero_map)

    for r in range(R):
      for c in range(C):
        if A[r][c] != 0 and A[r][c] != -1:  # 공기청정기 좌표, 벽처리 -> 개수 파악 k개
          diffusion = A[r][c] // 5
          k = 0
          for dr, dc in directions:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < R and 0 <= n_c < C:  # 바운더리 안에
              if A[n_r][n_c] != -1:  # 공기청정기 아니면
                k += 1
                draw[n_r][n_c] += diffusion
          draw[r][c] -= k * diffusion

    for r in range(R):
      for c in range(C):
        A[r][c] += draw[r][c]


  def clean():
    global A

    # 윗방향 반시계방향 돌기
    init = 0
    r, c = cleaner_up, 1
    clock_dr, clock_dc = 0, 1

    while (r, c) != (cleaner_up, 0):
      init, A[r][c] = A[r][c], init
      if (r, c) == (cleaner_up, C - 1):
        clock_dr, clock_dc = -1, 0
      elif (r, c) == (0, C - 1):
        clock_dr, clock_dc = 0, -1
      elif (r, c) == (0, 0):
        clock_dr, clock_dc = 1, 0
      r, c = r + clock_dr, c + clock_dc

    # 아랫방향 시계방향 돌기
    init = 0
    r, c = cleaner_down, 1
    clock_dr, clock_dc = 0, 1

    while (r, c) != (cleaner_down, 0):
      init, A[r][c] = A[r][c], init
      if (r, c) == (cleaner_down, C - 1):
        clock_dr, clock_dc = 1, 0
      elif (r, c) == (R - 1, C - 1):
        clock_dr, clock_dc = 0, -1
      elif (r, c) == (R - 1, 0):
        clock_dr, clock_dc = -1, 0
      r, c = r + clock_dr, c + clock_dc


  for _ in range(T):  # T초간
    spread()  # 확산
    clean()  # 공기청정

  print(sum([sum(a) for a in A]) + 2)  # 전체 합