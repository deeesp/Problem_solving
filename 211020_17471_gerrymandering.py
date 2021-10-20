import sys
from itertools import product
from collections import defaultdict

input = lambda: sys.stdin.readline()

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  A = [list(map(int, input().split())) for _ in range(N)]
  comb = []

  def set_param():
    # 범위 구하기
    for k in range(2,N): # 2 <= d1+d2 <= N-1
      d1 = 1
      d2 = k-d1
      for i in range(k):
        n_d1 = d1 + i
        n_d2 = d2 - i
        if n_d1 >= k:
          break
        if 1 <= n_d1 < N-1 and 1 <= n_d2 < N-1 and (n_d1, n_d2) not in comb:
          min_x, max_x, min_y, max_y = 1, N-n_d1-n_d2+1 , 1+n_d1, N-n_d2+1
          xy = list(product(range(min_x, max_x), range(min_y, max_y)))
          for x, y in xy:
            comb.append((x, y, n_d1, n_d2))


  def district(x, y, d1, d2):
    area = defaultdict(int)
    city = [[0]*N for _ in range(N)]
    start, end = y, y+1

    # 5번
    for i, r in enumerate(range(x, x+d1+d2+1)):
      start = y-i if i <= d1 else start+1
      end = y+1+i if i <= d2 else end-1
      for c in range(start, end):
        city[r-1][c-1] = 5
        area[5] += A[r-1][c-1]

    # 1번
    for r in range(1, x+d1):
      for c in range(1, y+1):
        if not city[r-1][c-1]:
          city[r-1][c-1] = 1
          area[1] += A[r-1][c-1]
        else:
          break

    # 3번
    for r in range(x+d1,N+1):
      for c in range(1, y-d1+d2):
        if not city[r-1][c-1]:
          city[r-1][c-1] = 3
          area[3] += A[r-1][c-1]
        else:
          break

    # 2번
    for r in range(1, x+d2+1):
      for c in range(N,y-1,-1):
        if not city[r-1][c-1]:
          city[r-1][c-1] = 2
          area[2] += A[r-1][c-1]
        else:
          break

    # 4번
    for r in range(N, x+d2-1,-1):
      for c in range(N,y-d1+d2-1,-1):
        if not city[r-1][c-1]:
          city[r-1][c-1] = 4
          area[4] += A[r-1][c-1]
        else:
          break

    min_area = min(area.values())
    max_area = max(area.values())
    return max_area - min_area


  min_answer = 9999999
  set_param()
  for n, (x, y, d1, d2) in enumerate(comb):
    min_answer = min(min_answer, district(x, y, d1, d2))

  print(min_answer)