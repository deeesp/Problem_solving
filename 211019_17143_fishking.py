import heapq
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline()
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  R, C, M = map(int, input().split())
  if not M:
    print(0)
    continue
  sharks = {n: list((map(int, input().split()))) for n in range(1, M+1)}  # 한 칸에 상어 최대 한 마리
  catched = dict()
  cur_point = 0
  dirs = {1: (-1,0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

  def fishing():
    candidate = []
    for key, (r, c, s, d, z) in sharks.items():
      if c == cur_point:
        heapq.heappush(candidate, (r, key, z))
    if candidate:
      col, n_shark, size = heapq.heappop(candidate)
      sharks.pop(n_shark)
      catched[n_shark] = size

  def move_sharks():
    overlap = defaultdict(list)
    for n_shark, (r, c, s, d, z) in sharks.items():
      n_r, n_c, n_d = r, c, d

      # 이동
      if n_d in [1,2]: # 상하
        iter_r = s % (2*(R-1))
        for _ in range(iter_r):
          n_r += dirs[n_d][0]
          if n_r<1:
            n_d = 2
            n_r += 2*dirs[n_d][0]
          elif n_r>R:
            n_d = 1
            n_r += 2*dirs[n_d][0]

      else: # 좌우
        iter_c = s % (2*(C-1))
        for _ in range(iter_c):
          n_c += dirs[n_d][1]
          if n_c<1:
            n_d = 3
            n_c += 2*dirs[n_d][1]
          elif n_c>C:
            n_d = 4
            n_c += 2*dirs[n_d][1]

      heapq.heappush(overlap[(n_r, n_c)], (-z, s, n_d, n_shark))

    for key, many_sharks in overlap.items(): # 가장 큰 상어가 살아남음
      r, c = key
      z, s, d, n_shark = heapq.heappop(many_sharks)
      sharks[n_shark] = [r, c, s, d, -z]
      for _, _, _, dead_n_shark in many_sharks:
        sharks.pop(dead_n_shark)

  while cur_point < C:
    cur_point += 1  # 1. 낚시왕 오른쪽 한칸 이동
    fishing()  # 2. 해당 열에 있는 상어 중 땅에서 가장 가까운 상어 잡음
    move_sharks()  # 3. 상어 이동 (속도 (칸/초), 이동하려는 방향

  print(sum([shark_size for shark_size in catched.values()]))

