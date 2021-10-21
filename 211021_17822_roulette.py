import sys
from collections import deque

input = lambda: sys.stdin.readline()

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  n, m, t = map(int, input().split())  # 2 <= N,M <= 50, 1 <= T <= 50
  A = [deque(map(int, input().split())) for _ in range(n)]  # 1~1000
  order = [list(map(int, input().split())) for _ in range(t)]  # x배수, d방향, k칸
  dirs = [(1,0), (0,-1)]

  def rotate(x, d, k):  # 원판 회전 독립적 돌아감
    # 1. x 배수 구하기
    candidates = [x*i-1 for i in range(1, n//x + 1)]
    # 2. 방향
    for r in candidates:
      for _ in range(k):  # k칸
        if d:  # 반시계
          A[r].append(A[r].popleft())
        else:  # 시계
          A[r].appendleft(A[r].pop())


  def check_neighbor():
    check = [[0]*m for _ in range(n)]
    # 인접수 같은지
    for i in range(n):
      for j in range(m):
        for dir in dirs:
          n_i, n_j = i+dir[0], j+dir[1]
          if n_i < n:
            if A[i][j] == A[n_i][n_j] and A[i][j]!=0 and A[n_i][n_j]!=0:
              check[i][j] = 1
              check[n_i][n_j] = 1

    # 같은 것 있으면 모두 지우기
    if sum([sum(roulette) for roulette in check]):
      for i, roulette in enumerate(check):
        for j, r in enumerate(roulette):
          if r:
            A[i][j] = 0
      return 1

    # 같은 것 없으면
    else: # 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
      cnt = n*m-sum([a.count(0) for a in A])
      if cnt:
        avg = sum([sum(a) for a in A])/cnt
        # print(cnt, avg)
        for i, roulette in enumerate(check):
          for j in range(m):
            if A[i][j]!=0 and A[i][j] > avg:
              A[i][j] -= 1
            elif A[i][j]!=0 and A[i][j] < avg:
              A[i][j] += 1
        return 1
      else:
        return 0


  for a, (x, d, k) in enumerate(order):
    # print(f'{a}번째')
    rotate(x, d, k)
    if not check_neighbor():
      break

  print(sum(sum(a)for a in A))
